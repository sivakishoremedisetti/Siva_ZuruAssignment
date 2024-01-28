import maya.cmds as cmds
import os


def script_run():
    if cmds.objExists('Cube'):
        cmds.delete('Cube')
    cmds.polyCube(sx=1, sy=1, sz=1, h=1, name="Cube")
    sel = cmds.ls(sl=True)
    for i in sel:
        cmds.addAttr(i, ln="ShowDuplicate", at="bool")
        cmds.setAttr(i + ".ShowDuplicate", e=True, keyable=True)
    cmds.select(cl=True)
    obj = sel[0]
    if cmds.objExists('CubeB'):
        cmds.delete('CubeB')
    cmds.duplicate(obj, name='CubeB')
    cmds.select(cl=True)
    cmds.select('CubeB')
    cmds.setAttr("CubeB.translateX", 10)

    cmds.addAttr('CubeB', ln="Duplicate", at="bool")
    cmds.setAttr("CubeB.Duplicate", e=True, keyable=True)
    cmds.connectAttr('Cube.ShowDuplicate', 'CubeB.visibility')
    cmds.connectAttr('Cube.ShowDuplicate', 'CubeB.Duplicate')
    if cmds.objExists('CubeB'):
        cmds.select('CubeB.f[0]', r=True)
        cmds.delete('CubeB.f[0]')
    cmds.select(cl=True)
    userpath = os.path.expanduser("~")
    custom_path = os.path.join(userpath, "test.ma").replace('/', '\\')
    cmds.file(rename=custom_path)
    cmds.file(save=True, force=True, type='mayaAscii')