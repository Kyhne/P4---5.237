clc; clear; close all;
Fs=2000; %sampling frequency
f=200; %frequency of the sound wave
dt=1/Fs;
sekunder=2; %Signalets længde

t=0:dt:sekunder-dt;
signal = sin(2*pi*t.^2*f);
% window = 100 means x is divided into segments of length 100 and each
% window is a hamming window
subplot(2, 1, 1);
spectrogram(signal,hamming(256),0,100,Fs,'yaxis');
title('Hamming window with length 256 and with 0% overlap');
disp(size(signal));
subplot(2,1,2);
spectrogram(signal,hamming(256),128,100,Fs,'yaxis'); %Syntax: spectrogram(sequence, window, nr. of overlapped samples, cyclical frequencies, sample-rate)
title('Hamming window with length 256 and with 50% overlap');


subplot(2,1,1);
spectrogram(signal,rectwin(256),0,100,Fs,'yaxis'); %Syntax: spectrogram(sequence, window, nr. of overlapped samples, cyclical frequencies, sample-rate)
title('Rectangular window with length 256 and with 0% overlap');

subplot(2,1,2);
spectrogram(signal,rectwin(256),128,100,Fs,'yaxis'); %Syntax: spectrogram(sequence, window, nr. of overlapped samples, cyclical frequencies, sample-rate)
title('Rectangular window with length 256 and with 50% overlap');

subplot(2,1,1);
spectrogram(signal,hann(256),128,100,Fs,'yaxis'); %Syntax: spectrogram(sequence, window, nr. of overlapped samples, cyclical frequencies, sample-rate)
title('Hann window with length 256 and with 50% overlap');

subplot(2,1,2);
spectrogram(signal,rectwin(256),128,100,Fs,'yaxis'); %Syntax: spectrogram(sequence, window, nr. of overlapped samples, cyclical frequencies, sample-rate)
title('Rectangular window with length 256 and with 50% overlap');

saveas(gcf,'hannandrectwindow.pdf')

