class FolderFolder:
    def __init__(self, path='.', levels=5,
                 file_filter=None, folder_filter=None,
                 collect_folder=None,
                 should_prune=True):
        from pathlib import Path
        from types import FunctionType
        if type(path) == str:
            self.path = Path(path)
        else:
            self.path = path
        assert self.path is not None, 'Path cannot be None'

        if folder_filter is None:
            folder_filter = lambda x: True
        elif type(folder_filter) != FunctionType:
            msg = 'Folder filter must be a function returning a boolean'
            raise ValueError(msg)

        self.files = []
        self.subfolders = []

        # Check if this folder should be collected
        if collect_folder is None:
            files = [y for y in self.path.iterdir() if y.is_file()]
            collect_folder = folder_filter(files)
        for x in self.path.iterdir():
            if x.is_dir():
                x_files = [y for y in x.iterdir() if y.is_file()]
                folder_pass = folder_filter(x_files)
            if (x.is_dir() and
               (folder_pass or any(y.is_dir() for y in x.iterdir())) and
               levels > 0):
                subfolder = FolderFolder(path=str(x), levels=levels - 1,
                                         file_filter=file_filter,
                                         folder_filter=folder_filter,
                                         collect_folder=folder_pass,
                                         should_prune=False)
                self.subfolders.append(subfolder)
            elif file_filter is not None and x.is_file() and file_filter(x):
                self.files.append(x)
            elif file_filter is None and collect_folder and x.is_file():
                self.files.append(x)

        # Use this flag to only run pruning once
        if should_prune:
            prune_result = self.prune()
            if prune_result is None:
                # The whole tree is empty
                self.subfolders = []
                self.files = []

    def prune(self):
        if len(self.subfolders) == 0:
            if len(self.files) == 0:
                return None
            else:
                return self
        else:
            new_subfolders = []
            for folder in self.subfolders:
                result = folder.prune()
                if result is not None:
                    new_subfolders.append(result)

            if len(self.files) != 0 or len(new_subfolders) != 0:
                self.subfolders = new_subfolders
                return self
            else:
                return None

    def __str__(self, start='\n---'):
        msg = str(self.path.absolute())

        for f in self.files:
            msg = msg + start + f.name

        for folder in self.subfolders:
            msg = msg + start
            msg = (msg +
                   folder.__str__(start=start + '---')
                   .replace(str(self.path.absolute()), ''))

        return msg

    def count_files(self):
        my_count = len(self.files)

        for folder in self.subfolders:
            my_count += folder.count_files()

        return my_count

    def map_files(self, fct):
        for f in self.files:
            fct(f)

        for folder in self.subfolders:
            folder.map_files(fct)

    def map_folders(self, fct):
        fct(self.files)

        for folder in self.subfolders:
            folder.map_folders(fct)

    def fold(self, fold_fct, acc):
        nacc = fold_fct(acc, self.files)

        for folder in self.subfolders:
            nacc = folder.fold(fold_fct, nacc)

        return nacc

    def remove_levels(self, nlevels):
        if nlevels <= 1:
            return self.subfolders
        else:
            results = [folder.remove_levels(nlevels - 1)
                       for folder in self.subfolders]
            from functools import reduce
            result = reduce(lambda a, b: a + b, results, [])
            return result

    def copy_folders(self, destination='.', rename_fct=None):
        import os
        import shutil
        from pathlib import Path

        def to_name(_path):
            return _path.name

        folder_name = to_name(self.path.absolute())
        dest_path = Path(destination).absolute()
        if not dest_path.is_dir():
            os.mkdir(str(dest_path))

        full_dest_name = str(dest_path.joinpath(folder_name).absolute())

        dest_subfolders = [to_name(x)
                           for x in dest_path.iterdir() if x.is_dir()]
        if folder_name not in dest_subfolders:
            os.mkdir(full_dest_name)

        for fobj in self.files:
            if rename_fct is not None:
                fname = fobj.name
                nfname = rename_fct(fname)
                ndest_name = str(dest_path.joinpath(folder_name)
                                          .joinpath(nfname)
                                          .absolute())
                shutil.copy2(str(fobj), ndest_name)
            else:
                shutil.copy2(str(fobj), full_dest_name)

        for folder in self.subfolders:
            folder.copy_folders(destination=full_dest_name,
                                  rename_fct=rename_fct)
