{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "def float2pcm(sig,dtype ='int16'):\n",
    "    sig = np.asarray(sig)\n",
    "    dtype = np.dtype(dtype)\n",
    "    i = np.iinfo(dtype)\n",
    "    abs_max = 2 ** (i.bits - 1)\n",
    "    offset = i.min + abs_max\n",
    "    return (sig * abs_max + offset).clip(i.min, i.max).astype(dtype)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "background recording ...\n",
      "background complete\n",
      "Actual recording ...\n",
      "Actual complete\n"
     ]
    },
    {
     "ename": "FileNotFoundError",
     "evalue": "[WinError 2] 系统找不到指定的文件。",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[15], line 41\u001b[0m\n\u001b[0;32m     37\u001b[0m write(\u001b[39m\"\u001b[39m\u001b[39msound_record\u001b[39m\u001b[39m\\\u001b[39m\u001b[39msound_recording.wav\u001b[39m\u001b[39m\"\u001b[39m, sample_freq, recording)\n\u001b[0;32m     39\u001b[0m \u001b[39m#Convert wav file to a wave module recognizable \u001b[39;00m\n\u001b[1;32m---> 41\u001b[0m background_alternate \u001b[39m=\u001b[39m AudioSegment\u001b[39m.\u001b[39;49mfrom_wav(\u001b[39m\"\u001b[39;49m\u001b[39msound_record/Background.wav\u001b[39;49m\u001b[39m\"\u001b[39;49m)\n\u001b[0;32m     42\u001b[0m background_alternate\u001b[39m.\u001b[39mexport(\u001b[39m\"\u001b[39m\u001b[39msound_record/background_output.wav\u001b[39m\u001b[39m\"\u001b[39m, \u001b[39mformat\u001b[39m\u001b[39m=\u001b[39m\u001b[39m\"\u001b[39m\u001b[39mwav\u001b[39m\u001b[39m\"\u001b[39m, codec\u001b[39m=\u001b[39m\u001b[39m\"\u001b[39m\u001b[39mpcm_s16le\u001b[39m\u001b[39m\"\u001b[39m)\n\u001b[0;32m     44\u001b[0m \u001b[39m#Fourier Transform ------------------------------------------------------------\u001b[39;00m\n\u001b[0;32m     45\u001b[0m \n\u001b[0;32m     46\u001b[0m \u001b[39m#Background wave open\u001b[39;00m\n",
      "File \u001b[1;32md:\\Coding Software\\Anaconda\\lib\\site-packages\\pydub\\audio_segment.py:808\u001b[0m, in \u001b[0;36mAudioSegment.from_wav\u001b[1;34m(cls, file, parameters)\u001b[0m\n\u001b[0;32m    806\u001b[0m \u001b[39m@classmethod\u001b[39m\n\u001b[0;32m    807\u001b[0m \u001b[39mdef\u001b[39;00m \u001b[39mfrom_wav\u001b[39m(\u001b[39mcls\u001b[39m, file, parameters\u001b[39m=\u001b[39m\u001b[39mNone\u001b[39;00m):\n\u001b[1;32m--> 808\u001b[0m     \u001b[39mreturn\u001b[39;00m \u001b[39mcls\u001b[39;49m\u001b[39m.\u001b[39;49mfrom_file(file, \u001b[39m'\u001b[39;49m\u001b[39mwav\u001b[39;49m\u001b[39m'\u001b[39;49m, parameters\u001b[39m=\u001b[39;49mparameters)\n",
      "File \u001b[1;32md:\\Coding Software\\Anaconda\\lib\\site-packages\\pydub\\audio_segment.py:728\u001b[0m, in \u001b[0;36mAudioSegment.from_file\u001b[1;34m(cls, file, format, codec, parameters, start_second, duration, **kwargs)\u001b[0m\n\u001b[0;32m    726\u001b[0m     info \u001b[39m=\u001b[39m \u001b[39mNone\u001b[39;00m\n\u001b[0;32m    727\u001b[0m \u001b[39melse\u001b[39;00m:\n\u001b[1;32m--> 728\u001b[0m     info \u001b[39m=\u001b[39m mediainfo_json(orig_file, read_ahead_limit\u001b[39m=\u001b[39;49mread_ahead_limit)\n\u001b[0;32m    729\u001b[0m \u001b[39mif\u001b[39;00m info:\n\u001b[0;32m    730\u001b[0m     audio_streams \u001b[39m=\u001b[39m [x \u001b[39mfor\u001b[39;00m x \u001b[39min\u001b[39;00m info[\u001b[39m'\u001b[39m\u001b[39mstreams\u001b[39m\u001b[39m'\u001b[39m]\n\u001b[0;32m    731\u001b[0m                      \u001b[39mif\u001b[39;00m x[\u001b[39m'\u001b[39m\u001b[39mcodec_type\u001b[39m\u001b[39m'\u001b[39m] \u001b[39m==\u001b[39m \u001b[39m'\u001b[39m\u001b[39maudio\u001b[39m\u001b[39m'\u001b[39m]\n",
      "File \u001b[1;32md:\\Coding Software\\Anaconda\\lib\\site-packages\\pydub\\utils.py:274\u001b[0m, in \u001b[0;36mmediainfo_json\u001b[1;34m(filepath, read_ahead_limit)\u001b[0m\n\u001b[0;32m    271\u001b[0m         file\u001b[39m.\u001b[39mclose()\n\u001b[0;32m    273\u001b[0m command \u001b[39m=\u001b[39m [prober, \u001b[39m'\u001b[39m\u001b[39m-of\u001b[39m\u001b[39m'\u001b[39m, \u001b[39m'\u001b[39m\u001b[39mjson\u001b[39m\u001b[39m'\u001b[39m] \u001b[39m+\u001b[39m command_args\n\u001b[1;32m--> 274\u001b[0m res \u001b[39m=\u001b[39m Popen(command, stdin\u001b[39m=\u001b[39;49mstdin_parameter, stdout\u001b[39m=\u001b[39;49mPIPE, stderr\u001b[39m=\u001b[39;49mPIPE)\n\u001b[0;32m    275\u001b[0m output, stderr \u001b[39m=\u001b[39m res\u001b[39m.\u001b[39mcommunicate(\u001b[39minput\u001b[39m\u001b[39m=\u001b[39mstdin_data)\n\u001b[0;32m    276\u001b[0m output \u001b[39m=\u001b[39m output\u001b[39m.\u001b[39mdecode(\u001b[39m\"\u001b[39m\u001b[39mutf-8\u001b[39m\u001b[39m\"\u001b[39m, \u001b[39m'\u001b[39m\u001b[39mignore\u001b[39m\u001b[39m'\u001b[39m)\n",
      "File \u001b[1;32md:\\Coding Software\\Anaconda\\lib\\subprocess.py:971\u001b[0m, in \u001b[0;36mPopen.__init__\u001b[1;34m(self, args, bufsize, executable, stdin, stdout, stderr, preexec_fn, close_fds, shell, cwd, env, universal_newlines, startupinfo, creationflags, restore_signals, start_new_session, pass_fds, user, group, extra_groups, encoding, errors, text, umask, pipesize)\u001b[0m\n\u001b[0;32m    967\u001b[0m         \u001b[39mif\u001b[39;00m \u001b[39mself\u001b[39m\u001b[39m.\u001b[39mtext_mode:\n\u001b[0;32m    968\u001b[0m             \u001b[39mself\u001b[39m\u001b[39m.\u001b[39mstderr \u001b[39m=\u001b[39m io\u001b[39m.\u001b[39mTextIOWrapper(\u001b[39mself\u001b[39m\u001b[39m.\u001b[39mstderr,\n\u001b[0;32m    969\u001b[0m                     encoding\u001b[39m=\u001b[39mencoding, errors\u001b[39m=\u001b[39merrors)\n\u001b[1;32m--> 971\u001b[0m     \u001b[39mself\u001b[39;49m\u001b[39m.\u001b[39;49m_execute_child(args, executable, preexec_fn, close_fds,\n\u001b[0;32m    972\u001b[0m                         pass_fds, cwd, env,\n\u001b[0;32m    973\u001b[0m                         startupinfo, creationflags, shell,\n\u001b[0;32m    974\u001b[0m                         p2cread, p2cwrite,\n\u001b[0;32m    975\u001b[0m                         c2pread, c2pwrite,\n\u001b[0;32m    976\u001b[0m                         errread, errwrite,\n\u001b[0;32m    977\u001b[0m                         restore_signals,\n\u001b[0;32m    978\u001b[0m                         gid, gids, uid, umask,\n\u001b[0;32m    979\u001b[0m                         start_new_session)\n\u001b[0;32m    980\u001b[0m \u001b[39mexcept\u001b[39;00m:\n\u001b[0;32m    981\u001b[0m     \u001b[39m# Cleanup if the child failed starting.\u001b[39;00m\n\u001b[0;32m    982\u001b[0m     \u001b[39mfor\u001b[39;00m f \u001b[39min\u001b[39;00m \u001b[39mfilter\u001b[39m(\u001b[39mNone\u001b[39;00m, (\u001b[39mself\u001b[39m\u001b[39m.\u001b[39mstdin, \u001b[39mself\u001b[39m\u001b[39m.\u001b[39mstdout, \u001b[39mself\u001b[39m\u001b[39m.\u001b[39mstderr)):\n",
      "File \u001b[1;32md:\\Coding Software\\Anaconda\\lib\\subprocess.py:1440\u001b[0m, in \u001b[0;36mPopen._execute_child\u001b[1;34m(self, args, executable, preexec_fn, close_fds, pass_fds, cwd, env, startupinfo, creationflags, shell, p2cread, p2cwrite, c2pread, c2pwrite, errread, errwrite, unused_restore_signals, unused_gid, unused_gids, unused_uid, unused_umask, unused_start_new_session)\u001b[0m\n\u001b[0;32m   1438\u001b[0m \u001b[39m# Start the process\u001b[39;00m\n\u001b[0;32m   1439\u001b[0m \u001b[39mtry\u001b[39;00m:\n\u001b[1;32m-> 1440\u001b[0m     hp, ht, pid, tid \u001b[39m=\u001b[39m _winapi\u001b[39m.\u001b[39;49mCreateProcess(executable, args,\n\u001b[0;32m   1441\u001b[0m                              \u001b[39m# no special security\u001b[39;49;00m\n\u001b[0;32m   1442\u001b[0m                              \u001b[39mNone\u001b[39;49;00m, \u001b[39mNone\u001b[39;49;00m,\n\u001b[0;32m   1443\u001b[0m                              \u001b[39mint\u001b[39;49m(\u001b[39mnot\u001b[39;49;00m close_fds),\n\u001b[0;32m   1444\u001b[0m                              creationflags,\n\u001b[0;32m   1445\u001b[0m                              env,\n\u001b[0;32m   1446\u001b[0m                              cwd,\n\u001b[0;32m   1447\u001b[0m                              startupinfo)\n\u001b[0;32m   1448\u001b[0m \u001b[39mfinally\u001b[39;00m:\n\u001b[0;32m   1449\u001b[0m     \u001b[39m# Child is launched. Close the parent's copy of those pipe\u001b[39;00m\n\u001b[0;32m   1450\u001b[0m     \u001b[39m# handles that only the child should have open.  You need\u001b[39;00m\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m   1453\u001b[0m     \u001b[39m# pipe will not close when the child process exits and the\u001b[39;00m\n\u001b[0;32m   1454\u001b[0m     \u001b[39m# ReadFile will hang.\u001b[39;00m\n\u001b[0;32m   1455\u001b[0m     \u001b[39mself\u001b[39m\u001b[39m.\u001b[39m_close_pipe_fds(p2cread, p2cwrite,\n\u001b[0;32m   1456\u001b[0m                          c2pread, c2pwrite,\n\u001b[0;32m   1457\u001b[0m                          errread, errwrite)\n",
      "\u001b[1;31mFileNotFoundError\u001b[0m: [WinError 2] 系统找不到指定的文件。"
     ]
    }
   ],
