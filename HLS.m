clc; clear; close all;


% lydsignalin
[stoej,Fs]=audioread(['C:\Users\Nikolai Lund Kühne\OneDrive - Aalborg Universitet\Uni\4. semester\P4 - Signaler og Systemer\ingridstoej.wav']); % Seed så støjen er den samme over alle forsøgende
[y,Fs]=audioread(['C:\Users\Nikolai Lund Kühne\OneDrive - Aalborg Universitet\Uni\4. semester\P4 - Signaler og Systemer\ingridnoisyrevisedHLS.wav']); % Seed så støjen er den samme over alle forsøgende

% [nylyd,Fs]=audioread(['C:\Users\Nikolai Lund Kühne\OneDrive - Aalborg Universitet\Uni\4. semester\P4 - Signaler og Systemer\noiseboth.wav']); % Seed så støjen er den samme over alle forsøgende
% [hearloss, Fs] = audioread(['C:\Users\Nikolai Lund Kühne\OneDrive - Aalborg Universitet\Uni\4. semester\P4 - Signaler og Systemer\testhuse.wav']);


Fs = 14700; 
% Seed = 1234;
% nylyd = downsample(y, 3,2); % 44.1kHz/3 = 14.7kHz syntax: downsample(array, factor, phase)
% stoej = awgn(nylyd,-5,'measured',Seed); % awgn = Add white gaussian noise --- syntax --> awgn(data, signal-to-noice-ratio, powertype)


% disp(size(data));
% y = [];
% y(1) = 0.003062383609*nylyd(1);
% y(2) = 0.003062383609*nylyd(2)+0.009187150829*nylyd(1)+2.361425149*y(1);
% y(3) = 0.003062383609*nylyd(3)+0.009187150829*nylyd(2)+0.009187150829*nylyd(1)+2.361425149*y(2)-1.911136410*y(1);
% y(4) = 0.003062383609*nylyd(4)+0.009187150829*nylyd(3)+0.009187150829*nylyd(2)+0.003062383609*nylyd(1)+2.361425149*y(3)-1.911136410*y(2)+0.5252121917*y(1);

% for n=5:size(nylyd);
% y(n) = 0.003062383609*nylyd(n)+0.009187150829*nylyd(n-1)+0.009187150829*nylyd(n-2)+0.003062383609*nylyd(n-3)+2.361425149*y(n-1)-1.911136410*y(n-2)+0.5252121917*y(n-3);
% end;
% disp(y(32340))
% antal_sekunder=length(nylyd)/Fs;
% disp(y(2));
subplot(2, 1, 1);
spectrogram(stoej,hann(256),128,100,Fs,'yaxis');
title('Noisy Signal');
subplot(2,1,2);
spectrogram(y,hann(256),128,100,Fs,'yaxis');
title('Revised Hearing Loss Simulator applied');
% 
% soundsc(nylyd,Fs);
% pause(antal_sekunder + 1);
% soundsc(y,Fs);


% subplot(3,1,1);
% spectrogram(stoej,hann(256),128,100,Fs,'yaxis'); %Syntax: spectrogram(sequence, window, nr. of overlapped samples, cyclical frequencies, sample-rate)
% title('Noisy Signal');
% set(gcf,'Position',[100 100 500 500])
% subplot(3,1,2);
% spectrogram(nylyd, hann(256), 128,100,Fs, 'yaxis')
% title('Frequency transposed and compressed signal')
% subplot(3,1,3);
% spectrogram(hearloss,hann(256),128,100,Fs,'yaxis'); %Syntax: spectrogram(sequence, window, nr. of overlapped samples, cyclical frequencies, sample-rate)
% title('Hearing Loss Simulator applied');
% a= fft(lyd)
% plot(abs(a));
% subplot(2,1,2);

% audiowrite('ingridstoej.wav',stoej,Fs);
 
% saveas(gcf,'ingridnoisyrevisedHLS.pdf')
