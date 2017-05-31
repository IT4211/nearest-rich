#-*- coding: utf8 -*-

from win32file import SetFileTime, CreateFile, CreateDirectory, CloseHandle, error
from win32file import GENERIC_READ, GENERIC_WRITE, OPEN_EXISTING, CREATE_NEW

import pytsk3 # raw image analysis and file system analysis
import pyewf  # ewf iamge file processing
import os
import imgconf
import cgitb
cgitb.enable(format='text')

class tsk():
    FILE_TYPE_LOOKUP = {
        pytsk3.TSK_FS_NAME_TYPE_UNDEF: "-",
        pytsk3.TSK_FS_NAME_TYPE_FIFO: "p",
        pytsk3.TSK_FS_NAME_TYPE_CHR: "c",
        pytsk3.TSK_FS_NAME_TYPE_DIR: "d",
        pytsk3.TSK_FS_NAME_TYPE_BLK: "b",
        pytsk3.TSK_FS_NAME_TYPE_REG: "r",
        pytsk3.TSK_FS_NAME_TYPE_LNK: "l",
        pytsk3.TSK_FS_NAME_TYPE_SOCK: "h",
        pytsk3.TSK_FS_NAME_TYPE_SHAD: "s",
        pytsk3.TSK_FS_NAME_TYPE_WHT: "w",
        pytsk3.TSK_FS_NAME_TYPE_VIRT: "v"}

    META_TYPE_LOOKUP = {
        pytsk3.TSK_FS_META_TYPE_REG: "r",
        pytsk3.TSK_FS_META_TYPE_DIR: "d",
        pytsk3.TSK_FS_META_TYPE_FIFO: "p",
        pytsk3.TSK_FS_META_TYPE_CHR: "c",
        pytsk3.TSK_FS_META_TYPE_BLK: "b",
        pytsk3.TSK_FS_META_TYPE_LNK: "h",
        pytsk3.TSK_FS_META_TYPE_SHAD: "s",
        pytsk3.TSK_FS_META_TYPE_SOCK: "s",
        pytsk3.TSK_FS_META_TYPE_WHT: "w",
        pytsk3.TSK_FS_META_TYPE_VIRT: "v"}

    ATTRIBUTE_TYPES_TO_PRINT = [
        pytsk3.TSK_FS_ATTR_TYPE_NTFS_IDXROOT,
        pytsk3.TSK_FS_ATTR_TYPE_NTFS_DATA,
        pytsk3.TSK_FS_ATTR_TYPE_DEFAULT]

    def __init__(self, url):
        self.url = url
        self._recursive = True
        self.extract_list = list()
        self.fullpath = list()

    def LoadImage(self):
        ewformat = ['.s01', '.E01', '.Ex01', '.e01']
        rawformat = ['.dd', '.raw', '.001']
        ext = os.path.splitext(self.url)

        if ext[1] in ewformat:
            filenames = pyewf.glob((self.url).decode('utf8'))
            ewf_handle = pyewf.handle()
            ewf_handle.open(filenames)
            img_info = ewf_Img_Info(ewf_handle)
            self.fs_info = pytsk3.FS_Info(img_info)

        elif ext[1] in rawformat:
            img_info = pytsk3.Img_Info(url = self.url)
            self.fs_info = pytsk3.FS_Info(img_info)

    def SetConf(self):
        self.conf = imgconf.extractconf()
        self.condition = self.conf[0]

    def ListDirectory(self, directory, stack=None, path_stack=None):
        stack.append(directory.info.fs_file.meta.addr)

        for directory_entry in directory:
            prefix = "+" * (len(stack) - 1)
            if prefix:
                prefix += " "

            # Skip ".", ".." or directory entries without a name.
            if (not hasattr(directory_entry, "info") or
                    not hasattr(directory_entry.info, "name") or
                    not hasattr(directory_entry.info.name, "name") or
                        directory_entry.info.name.name in [".", ".."]):
                continue

            # filtering
            self.PrintDirectoryEntry(directory_entry, prefix=prefix, path_stack=path_stack)

            if self._recursive:
                try:
                    sub_directory = directory_entry.as_directory()
                    path_stack.append(directory_entry.info.name.name)
                    name = directory_entry.info.name.name
                    inode = directory_entry.info.meta.addr

                    # This ensures that we don't recurse into a directory
                    # above the current level and thus avoid circular loops.
                    if inode not in stack:
                        self.ListDirectory(sub_directory, stack, path_stack)

                except IOError:
                    pass

        stack.pop(-1)
        if len(path_stack):
            path_stack.pop(-1)

    def OpenDirectory(self, inode_or_path):
        inode = None
        path = None
        if inode_or_path is None:
            path = "/"
        elif inode_or_path.startswith("/"):
            path = inode_or_path
        else:
            inode = inode_or_path

        # Note that we cannot pass inode=None to fs_info.opendir().
        if inode:
            directory = self.fs_info.open_dir(inode=inode)
        else:
            directory = self.fs_info.open_dir(path=path)

        return directory

    def PrintDirectoryEntry(self, directory_entry, prefix="", path_stack=list()):

        meta = directory_entry.info.meta
        name = directory_entry.info.name
        ext = os.path.splitext(name.name)

        if type(meta) != pytsk3.TSK_FS_META:
            return

        size = meta.size
        path = "/".join(path_stack)

        #filter , false -> return
        postfix = imgconf.infix_to_postfix(self.condition[1])

        postfix = postfix.replace('mtime', str(meta.mtime))\
            .replace('atime', str(meta.atime))\
            .replace('ctime', str(meta.crtime))\
            .replace('etime', str(meta.ctime))\
            .replace('ext', '"'+str(ext[1].replace(' ', ''))+'"')\
            .replace('size', str(size))\
            .replace('path', str(path))

        if not imgconf.search_condition(postfix):
            return

        maceTime = [meta.mtime, meta.atime, meta.crtime, meta.ctime]

        name_type = "-"
        if name:
            name_type = self.FILE_TYPE_LOOKUP.get(int(name.type), "-")

        meta_type = "-"
        if meta:
            meta_type = self.META_TYPE_LOOKUP.get(int(meta.type), "-")

        for attribute in directory_entry:
            inode_type = int(attribute.info.type)
            if inode_type in self.ATTRIBUTE_TYPES_TO_PRINT:
                if self.fs_info.info.ftype in [
                    pytsk3.TSK_FS_TYPE_NTFS, pytsk3.TSK_FS_TYPE_NTFS_DETECT]:
                    inode = "{0:d}".format(meta.addr)
                else:
                    inode = "{0:d}".format(meta.addr)

                attribute_name = attribute.info.name
                if attribute_name and attribute_name not in ["$Data", "$I30"]:
                    filename = "{0:s}:{1:s}".format(name.name, attribute.info.name)
                else:
                    filename = name.name

                if meta and name:
                    self.extract_list.append((inode, filename, maceTime, path))

    def debug_print_extlist(self):
        print self.extract_list

    def ExtractDirectoryEntry(self, path_option):

        self.debug_print_extlist()
        for i in self.extract_list:
            f = self.fs_info.open_meta(inode = int(i[0]))
            name = i[1]
            mace = i[2]
            path = i[3]

            offset = 0
            size = f.info.meta.size
            print "size: ", size
            #BUFF_SIZE = 800000000 #1024 * 1024

            while offset < size:
                available_to_read = size
                data = f.read_random(offset, available_to_read)
                if not data: break

                offset += len(data)

                try:
                    # path option
                    if path_option:
                        if f.info.meta.type == pytsk3.TSK_FS_META_TYPE_DIR:
                            path = os.path.join("./output/", path, name).decode('utf-8')
                            os.mkdir(path)
                        else:
                            path = os.path.join("./output/", path).decode('utf-8')
                            print "[open:path]", path
                            if not os.path.isdir(path):
                                os.makedirs(path)
                            name = name.decode('utf-8')
                            filename = os.path.join(path, name)
                            print "[open:filename]", filename
                            output = open(filename, "w")
                            output.write(data)
                            output.close()
                    else:
                        if f.info.meta.type == pytsk3.TSK_FS_META_TYPE_DIR:
                            path = os.path.join("./output/", name).decode('utf-8')
                            os.mkdir(path)
                        else:
                            filename = os.path.join("./output/", name).decode('utf-8')
                            output = open(filename, "w")
                            output.write(data)
                            output.close()

                    print "[debug:Path]", path

                except IOError as emsg:
                    print "[debug:except]", emsg

                finally:

                    if f.info.meta.type == pytsk3.TSK_FS_META_TYPE_DIR:
                        pass
                    else:
                        try:
                            print "[debug:CreateFile]", filename
                            fh = CreateFile(filename, GENERIC_READ | GENERIC_WRITE, 0, None, OPEN_EXISTING, 0, 0)
                            SetFileTime(fh, mace[0], mace[1], mace[2], mace[3])
                            CloseHandle(fh)
                        except OverflowError as e:
                            print e
                            pass

                        except error, e:
                            print "[err] Timestamp can not be modified due to file name issue"
                            pass


class ewf_Img_Info(pytsk3.Img_Info):
    def __init__(self, ewf_handle):
        self._ewf_handle = ewf_handle
        super(ewf_Img_Info, self).__init__(
            url="", type=pytsk3.TSK_IMG_TYPE_EXTERNAL)

    def close(self):
        self._ewf_handle.close()

    def read(self, offset, size):
        self._ewf_handle.seek(offset)
        return self._ewf_handle.read(size)

    def get_size(self):
        return self._ewf_handle.get_media_size()
