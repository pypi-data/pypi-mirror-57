
import soundfile as sf

class AudioIO:
    def __init__(self, fileName):
        """
        Read and Write audio data from .wav file in current working directory. 

        Parameter:
        
        fileName : string
            Name of .wav file to be read. 
        """
        self.file_name = fileName
        self.data = self.readWav()
        length_seconds = round(len(self.data) / self.sample_rate, 2)
        if len(self.data.shape) == 2:
            raise Exception ("Imported audio file should be mono, not stereo.")
        if len(self.data.shape) == 2:
            channels = 'stereo'
        else:
            channels = 'mono'
        print("Loaded {} | Sample Rate : {} | Channels : {} | Length : {}s".format(self.file_name, self.sample_rate, channels, length_seconds))

    def readWav(self):
        """
        Return PCM amplitude data in data as type numpy array.

        Automatically updates the sample_rate parameter with sample rate of imported audio.
        """
        wav = sf.read(self.file_name)
        self.sample_rate = wav[1]
        return wav[0]

    def writeWav(self, fileName, signal):
        """
        Write numpy array to new wav file. 

        Parameters: 

        fileName : string
            Name of new wav file. (Include .wav extension)

        signal : Numpy array
            Array containing audio data.
        """
        if len(signal.shape) == 2:
            channels = 'stereo'
        else:
            channels = 'mono'
        length_seconds = round(len(signal) / self.sample_rate, 2)
        print("Writing {} | Sample Rate : {} | Channels : {} | Length : {}s".format(fileName, self.sample_rate, channels, length_seconds))
        sf.write(fileName, signal, self.sample_rate)