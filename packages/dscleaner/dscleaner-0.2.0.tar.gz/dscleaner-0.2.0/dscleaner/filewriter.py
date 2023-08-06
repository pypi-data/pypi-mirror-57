from .utils import path_splitter
import os
import pyemddf
import pandas as pd
class FileWriter:
    """
        Writes to a file.

        The class should be instantiated with a ``with`` statement.

        Args:
            file: Accepts either a FileUtil, or IFileInfo Specialization.
            mode: Allows for `w` for writing or `a` for appending.
    """
    def __init__(self,file, mode = 'w'):
        from .ifileinfo import IFileInfo
        from .fileutil import FileUtil
        if(issubclass(type(file),IFileInfo)):
            self.file = file 
        elif(issubclass(type(file),FileUtil)):
            self.file = file.file
        else:
            raise TypeError("Wrong argument type")
        
        self.mode = mode

    def __enter__(self):
        return self

    def __exit__(self,type,value,traceback):
        self.close()
    def close(self):
        #self.file.close()
        pass
        
    def create_file(self,new_filepath,samplerate = None):
        """
            Creates a new file with the extension given in ``new_filepath``.

            If the source file isn't a soundfile the target file will not be well formated.

            In order to normalize, you should run ``FileUtil.standardize`` method before.

            Args:
                new_filepath - The diretory and name the new file will have,
                    it will convert based on file extension.
                samplerate (Optional) - The samplerate the file should have,
                    if not supplied it will use the own `file` samplerate.
        """

        file_exists = (os.path.isfile(new_filepath))
        if(samplerate == None):
            samplerate = self.file.getSamplerate()
        path = path_splitter(new_filepath)
        if(path['file_name'] == None):
            raise TypeError("It doesn't contain a filename")
        try:
            os.mkdir(path['path'])
            #tries to create the directory
        except (OSError,FileNotFoundError) as e:
            pass
        if(path['extension']=='csv'):
            pd.DataFrame(self.file.getSamples()).to_csv(path['full_path'], header= None,index = None)
        else:
            import soundfile as sf
            if(self.mode == 'a' and file_exists):
                with sf.SoundFile(path['full_path'], mode = 'r+') as wfile:
                    wfile.seek(0,sf.SEEK_END)
                    wfile.write(self.file.getSamples())
            else:
                sf.write(path['full_path'], self.file.getSamples(), samplerate,format=path['extension']) # writes to the new file 
            return

    def create_file_EMDDF(self, new_filepath, json_file, samplerate = None):
        """
            Creates a soundfile with the EMD-DF format, recurs to the ``pyemddf`` package
            
            NOTE: 
                Only works on wave and wave64 files.

            Args:
                samplerate(optional): Samplerate of the file.
                json_file: a JSON file with the metadata fields, you can get a template 
                for it by executing ``pyemddf.create_template_file()``.
        """
        if(not(os.path.exists(json_file))): raise FileNotFoundError("There is no file called" + json_file)
        self.create_file(new_filepath,samplerate)
        path = path_splitter(new_filepath)
        pyemddf.addChunks(path['full_path'],json_file)