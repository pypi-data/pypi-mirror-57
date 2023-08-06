import soundfile as sf
import tempfile
import os
from .ifileinfo import IFileInfo

class FileInfo(IFileInfo):
    """
        Defines the class to manipulate soundfiles.


        Receives a path to a file.

        Copies the file to a temporary location.

        Gets edited through the FileUtil.

        FileWriter converts and writes to another location.


        NOTE:
            - close method MUST always be called or else the temporary file stays in disk.
            - ``with`` statements should be used in order to close the files automatically.

    """
    def __init__(self,path):
        super().__init__(path)
        self._path = path #ACTUAL FILE
        self._tmpPath = tempfile.gettempdir() #TEMPORARY COPY

        try:
            import shutil
            self._tmpPath = shutil.copy(self._path,self._tmpPath)
        except FileExistsError:
            print("FEXISTS l28")
            pass
        self._initinfo()

    def __enter__(self):
        return self

    def __exit__(self,type,value,traceback):
        self.close()

    def _initinfo(self):
        with sf.SoundFile(self._tmpPath, mode ='r') as rfile:
            self._samplerate = rfile.samplerate
            self._frames = rfile.read()
            self._numchannels = rfile.channels
        return

    #================READ METHODS ==================#

    def getFilepath(self):
        """
            See the base class ``ifileinfo``.
        """
        return self._path

    def getNumberOfFrames(self):
        """
            See the base class ``ifileinfo``.
        """
        return len(self.getSamples())
            
    def getSamplerate(self):
        """
            See the base class ``ifileinfo``.
        """
        return self._samplerate

    def getNumberOfChannels(self):
        """
        Returns:
            Number of channels the file has.
        """
        return self._numchannels

    def getDuration(self):
        """
        Returns:
            The duration of the file in seconds.
        """
        return self.getNumberOfFrames()/self.getSamplerate()

    def get_rounded_duration(self):
        """
            Returns:
                The rounded duration in seconds.
        """
        from math import ceil
        rounded_duration = ceil(self.getDuration()) #in seconds
        return rounded_duration 
    
    def getSamples(self):
        """
        Reads all of the samples in the file

        Returns: 
            numpy array containing the samples.
        """
        return self._frames
        
    #================WRITE METHODS ==================#

    def setSamples(self, samples, samplerate = None):
        """
            Writes the ´samples´ as the new samples in the file.

            Args:
                samples: numpy array shaped like (n,c), where c is the number of channels.
                samplerate: the new sample rate the file will have, if none it will use the initial samplerate.
        """ 
        if (samplerate == None):
            samplerate = self.getSamplerate()
        samples = self._soundfile_array_converter(samples)
        with sf.SoundFile(self._tmpPath, mode = 'w', samplerate = self.getSamplerate(), channels = self.getNumberOfChannels()) as wfile:
            wfile.truncate(0) #removes all the samples in the file                
        sf.write(self._tmpPath,samples,samplerate)
        self._initinfo()

    def truncate(self,num_frames):
        """
            Truncates the file to only have ``num_frames``.
        """
        #with sf.SoundFile(self._tmpPath, mode = 'w', samplerate = self.getSamplerate(), channels = self.getNumChannels()) as wfile:
        #   wfile.truncate(num_frames)
        self.setSamples(self.getSamples()[:num_frames])
        self._initinfo()

    def addSamples(self,samples):
        """
            Appends the samples to the file.

            Similar to ´setSamples()´ but appends instead of truncating.
            See the base class ``ifileinfo``.

        """ 

        samples = self._soundfile_array_converter(samples)
        with sf.SoundFile(self._tmpPath, mode = 'r+') as wfile:
            wfile.seek(0,whence = sf.SEEK_END)
            wfile.write(samples)

    #================MISC METHODS ==================#
 
    def _soundfile_array_converter(self,array):
        """
            Checks if it has the correct array shape to be worked by pysoundfile.
            If not, it will transpose de array.
            Arguments:
                array: ndarray to convert.
            Returns:
                array: the converted array.
        """
        if(array.shape[1] > 20): #meaning it doesnt represent the number of channelsnumber of channels
            array = array.T
        return array
    
    def close(self):
        """
            Must always be called or the file won't be accessible by other processes AND the temp file will stay in disk.
            See the base class ``ifileinfo``.

        """
        import os
        try:
            os.unlink(self._tmpPath)

        except expression as identifier:
            print("err", identifier)
