from .fileinfo import FileInfo
from . import ifileinfo, filewriter, CsvFileInfo, utils
import numpy as np
import os
import soundfile as sf

class Merger():
    """
            Merger allows for creation of an empty soundfile to store multiple datasets easily.
            
            NOTE:
                W64 filetype is recommended, given it can store up to 18 exabytes of data.

            Args:
                channels: Number of channels the files parsed should have.
                path: the path where the new merger file should be created.
                samplerate: samplerate to write on the file.
                cutoff: how often should the file be written **NOT IMPLEMENTED**
                    (eg. for each 1024MB of data reached a new file is created)
                mode: either 'a' or 'w' if the file should be appended or truncated, respectively.
                    Default behavior: append
    """
    def __init__(self, channels, path, samplerate, cutoff = None, mode='a'):
        
        self._channels = channels
        self._init_samples()
        if(isinstance(samplerate,int)):
            self._samplerate = samplerate
        else:
            raise TypeError("Samplerate not integer")
        self.path = path

        #if the file exists already, then there's no need to create it(FileInfo)
        #if theres no file, we need to create it (array)
        self.file_exists = (os.path.isfile(self.path))

        self.mode = mode

    def _init_samples(self):
        self._samples = np.empty(shape=(0,self._channels))

    def __enter__(self):
        return self

    def __exit__(self,type,value,traceback):
        pass

    def add(self, *files):
        """
            Adds new samples to the buffer array.

            When ``create_file`` method is executed the buffer gets emptied.

        Args:
            *files: An array, containing several pathes to files or IFileInfos specializations,
                although the latter is preferred.
        """
        tmp = None
        for f in files:
            if(issubclass(type(f),ifileinfo.IFileInfo)):
                tmp = f.getSamples()
            else:
                with FileInfo(f) as this:
                    tmp = this.getSamples()
            self._samples = np.append(self._samples,tmp,axis=0)
            #if(sys.getsizeof(self._samples) > (2**29)): escreve no ficheiro; para tal é necessário ter o ficheiro pré definido
            #adicionar 2**29(512MB) como cutoff

    def create_file(self, samplerate = None):
        """
            Creates a new file with the filename, converts based on extension given in ``new_filename``
            
            When executed the sample buffer will be emptied,
            so ``create_file`` should be executed frequently.

            Args:
                samplerate: Samplerate of the file.

        """
        if(len(self._samples) == 0):
            raise TypeError("No samples are queued!")
        if(samplerate == None):
            samplerate = self._samplerate
        path = utils.path_splitter(self.path)
        if(path['file_name'] == None):
            raise TypeError("It doesn't contain an extension")
        #tries to create the directory
        try: 
            import os
            os.mkdir(path['path'])
        except (OSError,FileNotFoundError) as e:
            #import errno
            pass
            #if(e.errno != errno.EEXIST):
            #   raise #if there's an error thats not eexits(file/directory exists)
        #Appends or simply write over the file based on mode 
        if(self.mode == 'a' and self.file_exists == True):
            with sf.SoundFile(path['full_path'], mode = 'r+') as wfile:
                wfile.seek(0,sf.SEEK_END)
                wfile.write(self._samples)
            self._init_samples()

        else: 
            with CsvFileInfo(self._samples,self._samplerate) as infofile:
                self.file_exists = True
                self._init_samples()
                with filewriter.FileWriter(infofile) as fw:
                    fw.create_file(path['full_path'], self._samplerate)

