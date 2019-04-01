clear all
close all
%load necg
%load prcp_12754.mat
%load fantasia_f1y06.mat
load mitdb_101.mat
%% load data
%ecg=s103_c;
fs = 360;
ecg0 = M_phase(2*fs:end);
ecg0 = ecg0'*1000;
%parameter
%例子中采样率360Hz，我们用的是100Hz
%time vector
len=length(ecg0);
t=1/fs:1/fs:len/fs;
%%
plot(t,ecg0);
xlabel('s');
ylabel('ECG');
%pick 3~5s of the data and do self-correlation
%in this case we choose 3s, which is 1080 samples
sl=3*fs;
t=t(1:sl);
ecg0=ecg0(fs:fs+sl-1);
for i=fix(0.2*fs):(sl/2)
    %sc(i)=ecg(1:sl/2)*ecg(i:sl/2+i-1)';
    sc(i)=ecg0(1:sl/2)*ecg0(i:sl/2+i-1)';
end
hold on
figure(2)
plot(t(1:sl/2),sc(1:sl/2));
xlabel('s');
ylabel('sc');

rr = [];
[~,index] = max(sc);
[~,ecg_index] = max(ecg0(1:(index-1)));
%figure(1)
%hold on
%plot((ecg_index)/fs,ecg0(ecg_index),'ro')
%rr(1) = ecg_index/fs

ecg0 = M_phase(2*fs:end);
ecg0 = ecg0'*1000;
%ecg0=ecg0(51:(10*fs+50));
st = 1;
interval = index;
i = 0;
while(st+interval<length(ecg0))
    i = i+1;
    [~,ecg_index] = max(ecg0(st:(st+interval)));
    figure(1)
    hold on
    rr(i) = (ecg_index+st-1)/fs;
    rr_index(i)=ecg_index+st-1;
    plot((rr_index(i))/fs,ecg0(rr_index(i)),'ro');
    st = st+interval;
end

length(rr)

rr_interval=diff(rr);
rr_interval(rr_interval<0.5)=[];
rr_interval(rr_interval>1.2)=[];

%the peak of the sc exists at 0.86s
%which means the average heart rate during(1s~3s)is 1/0.86s (~70b/min)
%寻找最大值可以在一定范围内寻找，具体范围根据生活中正常心率范围定

fid = fopen('mitdb_101.txt','w');
for i = 1:length(rr_interval)
    fprintf(fid,'%.0f\r\n',rr_interval(i)*1000);
end
fclose(fid);
