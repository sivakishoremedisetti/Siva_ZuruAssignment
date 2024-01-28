import os, sys, re
import subprocess


def run_job():
    maya_ver = ['Maya2020', 'Maya2022', 'Maya2023', 'Maya2024']
    for each in maya_ver:
        maya_batch = "C:/Program Files/Autodesk/" + each + "/bin/mayabatch.exe"
        if os.path.exists(maya_batch):
            break
        else:
            print("Maya path not found")
    application = maya_batch

    command = '\"{app}\" -command \"python(\\"from script_job import run_script;run_script()\\")\"'.format(
        app=application)
    print(command)

    module_path = os.path.dirname(os.path.dirname(__file__))

    if os.environ.get("PYTHONPATH"):
        os.environ["PYTHONPATH"] = "{};{}".format(os.environ["PYTHONPATH"], module_path)

    else:
        os.environ["PYTHONPATH"] = module_path
    result, error = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE).communicate()

    if error:
        print("error running subprocess error is below:\n{}".format(error))
        return False


if __name__ == '__main__':
    run_job()
