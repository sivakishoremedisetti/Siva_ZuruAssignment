import datetime
import json
import os.path
from pathlib import Path


def pysl(*args, **kwargs):
    """

    :param args:
    :param kwargs:
    :return:
    """
    json_data = json.load(open(json_path, 'r'))
    json_contents = json_data['contents']
    first_level_keys = [i['name'] for i in json_contents]
    json_contents = [i for i in json_contents if i['name'] not in ['.gitignore']]
    if args:
        if len(args) == 1:
            if args[0] in ['-A']:
                return first_level_keys
            elif args[0] in ['-l']:
                first_level_data = [return_values(i) for i in json_contents]
                return first_level_data
            elif args[0] in ['-help']:
                help_data = """
                1) pyls()
                   out put:LICENSE, README.md, ast, go.mod, lexer, main.go, parser, token
                
                2)pyls(A) NOTE : add .gitignore directory also
                  out put:.gitignore, LICENSE, README.md, ast, go.mod, lexer, main.go, parser, token
                
                3)pyls(l)  NOTE:First column corresponds to permissions, 2nd column corresponds to size, 3rd   to 5th 
                is date and time, and the last is file or directory name.
                  out put:
                
                    -rw-r--r-- 1071 Nov 14 11:27 LICENSE
                    -rw-r--r-- 83 Nov 14 11:27 README.md
                    drwxr-xr-x 4096 Nov 14 15:58 ast
                    -rw-r--r-- 60 Nov 14 13:51 go.mod
                    drwxr-xr-x 4096 Nov 14 15:21 lexer
                    -rw-r--r-- 74 Nov 14 13:57 main.go
                    drwxr-xr-x 4096 Nov 17 12:51 parser
                    drwxr-xr-x 4096 Nov 14 14:57 token
                
                4)pyls(l,r)  NOTE: r argument is reverse same as point 3
                
                  out put:
                    
                    drwxr-xr-x 4096 Nov 14 14:57 token
                    drwxr-xr-x 4096 Nov 17 12:51 parser
                    -rw-r--r-- 74 Nov 14 13:57 main.go
                    drwxr-xr-x 4096 Nov 14 15:21 lexer
                    -rw-r--r-- 60 Nov 14 13:51 go.mod
                    drwxr-xr-x 4096 Nov 14 15:58 ast
                    -rw-r--r-- 83 Nov 14 11:27 README.md
                    -rw-r--r-- 1071 Nov 14 11:27 LICENSE
                
                5)pyls(l,r,t)  NOTE:Implement the argument 't' that prints the results sorted by time_modified 
                (oldest first)
                
                  out put:
                
                    drwxr-xr-x 4096 Nov 17 12:51 parser
                    drwxr-xr-x 4096 Nov 14 15:58 ast
                    drwxr-xr-x 4096 Nov 14 15:21 lexer
                    drwxr-xr-x 4096 Nov 14 14:57 token
                    -rw-r--r-- 74 Nov 14 13:57 main.go
                    -rw-r--r-- 60 Nov 14 13:51 go.mod
                    -rw-r--r-- 1071 Nov 14 11:27 LICENSE
                    -rw-r--r-- 83 Nov 14 11:27 README.md
                
                6)pyls(l,r,t,filter=dir) NOTE: The only valid options are file and dir. Giving any other options should 
                print out helpful error message.
                  
                  out put:
                    drwxr-xr-x 4096 Nov 17 12:51 parser
                    drwxr-xr-x 4096 Nov 14 15:58 ast
                    drwxr-xr-x 4096 Nov 14 15:21 lexer
                    drwxr-xr-x 4096 Nov 14 14:57 token
                  pyls(l,r,t,filter=file)
                    -rw-r--r-- 74 Nov 14 13:57 main.go
                    -rw-r--r-- 60 Nov 14 13:51 go.mod
                    -rw-r--r-- 1071 Nov 14 11:27 LICENSE
                    -rw-r--r-- 83 Nov 14 11:27 README.md
                
                7)pyls(l,parser) NOTE: The output will be the contents of the parser subdirectory under interpreter 
                directory
                  out put:
                    -rw-r--r-- 533 Nov 14 16:03 go.mod
                    -rw-r--r-- 1622 Nov 17 12:05 parser.go
                    -rw-r--r-- 1342 Nov 17 12:51 parser_test.go
                  pyls(l parser/parser.go)
                  out put:
                         -rw-r--r-- 1622 Nov 17 12:05 ./parser/parser.go
                
                8)pyls(help)
                    out put:
                        #should print a helpful message.
                        # should include description and usage
                        # should list all available commands with choices where applicable"""
                return help_data

        elif len(args) == 2:
            if args[0] in ['-l'] and args[1] in ['-r']:
                reversed_first_level_data = [return_values(i) for i in reversed(json_contents)]
                return reversed_first_level_data
            elif args[0] in ['-l'] and args[1] in first_level_keys:
                parser_contents = [i for i in json_contents if i['name'] in [args[1]]]
                parser_data = [return_values(i) for i in parser_contents[-1]['contents']]
                return parser_data
            elif args[0] in ['-l'] and Path(args[1]).is_file():
                directory = os.path.basename(os.path.dirname(args[1]))
                parser_contents = [i for i in json_contents if i['name'] in [directory]]
                parser_data = [return_values(i) for i in parser_contents[-1]['contents']]
                parser_data = [i for i in parser_data if i[-1] == args[1]]
                return parser_data

        elif len(args) == 3:
            if args[0] in ['-l'] and args[1] in ['-r'] and args[2] in ['-t']:
                sorted_by_time_data = sorted([return_values(i) for i in json_contents], key=lambda x: x[2],
                                             reverse=True)
                if not kwargs:
                    return sorted_by_time_data
                else:
                    if len(kwargs) == 1 and 'filter' in kwargs and kwargs['filter'] in ['file', 'dir']:
                        if kwargs['filter'] in ['dir']:
                            filtered_data = [i for i in sorted_by_time_data if i[-1] and Path(i[-1]).is_dir()]
                        else:
                            filtered_data = [i for i in sorted_by_time_data if i[-1] and Path(i[-1]).is_file()]
                        return filtered_data
                    else:
                        print('Provided Arguments are wrong, Please check\n valid:\n\tl, \n\tr, \n\tfilter=file/dir')
                        return None

    else:
        if '.gitignore' in first_level_keys:
            first_level_keys.remove('.gitignore')
        return first_level_keys


def return_values(data_dict):
    order_keys = ['permissions', 'size', 'time_modified', 'name']
    return [
        datetime.datetime.fromtimestamp(data_dict[i]).strftime('%b %d %H:%M') if i in ['time_modified']
        else str(data_dict[i]) for i in order_keys
    ]


if __name__ == '__main__':
    valid = False
    while not valid:
        source_path = os.path.dirname(os.path.dirname(__file__))
        json_path = source_path+'//JsonParser//structure.json'
        if str(json_path).endswith('.json') and Path(json_path).exists():
            valid = True
        else:
            print('"%s" is not valid json file path, Please check and provide proper path' % json_path)

    # output = pysl()
    import sys
    if len(sys.argv) == 1:
        output1 = pysl()
        print(" ".join(output1))
        sys.exit()
    elif len(sys.argv) == 2:
        aa = (sys.argv[1])
        if len(aa)>2:
            output = pysl(aa)
            print("".join(output))
            sys.exit()
        output = pysl(aa)
    elif len(sys.argv) == 3:
        aa = (sys.argv[1:])
        output = pysl(aa[0],aa[1])
    elif len(sys.argv) == 4:
        aa = (sys.argv[1:])
        output = pysl(aa[0],aa[1],aa[2],filter='dir')
    if output:
        for each in output:
            print(''.join(each))
    else:
        print(output)
