# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['my_cli_tool/cli.py'],
    pathex=['/Users/avi.varma/dev/my_cli_tool'],
    binaries=[],
    datas=[
        ('my_cli_tool/file_manager.py', 'my_cli_tool'),
        ('my_cli_tool/config_manager.py', 'my_cli_tool')
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='mycli',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='mycli',
)
