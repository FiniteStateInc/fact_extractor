'''
This plugin unpacks avm file system container
'''
from common_helper_process import execute_shell_command
from helperFunctions.shell_utils import shell_escape_string

NAME = 'avm_sqfs_fake'
MIME_PATTERNS = ['filesystem/avm-sqfs-fake']
VERSION = '0.1'


def unpack_function(file_path, tmp_dir):
    output = execute_shell_command('dd if={} of={}/image.ext2 bs=256 skip=1 conv=sync'.format(shell_escape_string(file_path), shell_escape_string(tmp_dir)))
    return {'output': output}


# ----> Do not edit below this line <----
def setup(unpack_tool):
    for item in MIME_PATTERNS:
        unpack_tool.register_plugin(item, (unpack_function, NAME, VERSION))
