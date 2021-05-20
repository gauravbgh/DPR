import re
import datetime

abc= datetime.date.today()

with open('area-3.txt') as f:
    ar3 = f.readlines()

with open('area-1.txt') as f:
    ar1 = f.readlines()
    
with open('area-4.txt') as f:
    ar4 = f.readlines()
    
ar3_split= [x.replace('\n','') for x in ar3 if len(x)>1]
ar1_split= [x.replace('\n','') for x in ar1 if len(x)>1]
ar4_split= [x.replace('\n','') for x in ar4 if len(x)>1]

def monitored_well(dpr_list):
    indx= dpr_list.index([ i for i in dpr_list if re.search('.*[mM]onitored.*', i)][0])
    mon_well= dpr_list[indx+1].rstrip('.')
    return (mon_well)

def tpr(dpr_list):
    try:
        indx= dpr_list.index([ i for i in dpr_list if re.search('\*TPR.*', i)][0])
        if len(dpr_list[indx])>7:
            tpr= dpr_list[indx].split(' ')[-1]
            tpr= tpr.rstrip('.')
        else:
            tpr= dpr_list[indx+1].rstrip('.')
        tpr= tpr.replace(' ','')
        return(tpr)
    except IndexError:
        return ('')
    
    
def remark(dpr_list):
    remarks=[]
    ind_remark= dpr_list.index([ i for i in dpr_list if re.search('[rR]emarks.*', i)][0])
    ind_pressure= dpr_list.index([ i for i in dpr_list if re.search('[wW]ell\s?head .*', i)][0])
    for i in range(1, (ind_pressure-ind_remark)):
        remark= dpr_list[ind_remark+i]
        key= re.search('(\d+.) (\*.+\*)(\s?:?\s?)(.+)', remark)
        well_no = (key.group(2)).strip('*').rstrip(':')
        remarks.append('*{0}:* {1}'.format(well_no, key.group(4)))
    return(remarks)

def wellhead_press(dpr_list):
    start= dpr_list.index([ i for i in dpr_list if re.search('[wW]ell\s?head .*', i)][0])
    stop= dpr_list.index([ i for i in dpr_list if re.search('[rR]egard.*', i)][0])
    out= dpr_list[(start+1):stop]
    return(out)

if len(ar4_split)>4:
    total_wells_monitored= monitored_well(ar1_split)+(',\n')+monitored_well(ar3_split)+(',\n')+monitored_well(ar4_split)+('.')
    tpr_total= tpr(ar1_split) + (',') + tpr(ar3_split) + ('.') + tpr(ar4_split)
    total_remarks= remark(ar1_split)+remark(ar3_split)+remark(ar4_split)
    remarks_print= ''
    for i in range(len(total_remarks)):
        remarks_print= remarks_print + str(i+1) + ') ' + total_remarks[i]+ '\n'
    total_pressure= wellhead_press(ar1_split)+ wellhead_press(ar3_split)+ wellhead_press(ar4_split)
    pressures= ''
    for i in range(len(total_pressure)):
        pressures= pressures + total_pressure[i]+ '\n'
else:
    total_wells_monitored= monitored_well(ar1_split)+(',\n')+monitored_well(ar3_split)+('.')
    tpr_total= tpr(ar1_split) + (',') + tpr(ar3_split) + ('.')
    total_remarks= remark(ar1_split)+remark(ar3_split)
    remarks_print= ''
    for i in range(len(total_remarks)):
        remarks_print= remarks_print + str(i+1) + ') ' + total_remarks[i]+ '\n'
    total_pressure= wellhead_press(ar1_split)+ wellhead_press(ar3_split)
    pressures= ''
    for i in range(len(total_pressure)):
        pressures= pressures + total_pressure[i]+ '\n'
        
final= """Sir,
*A/Lift DPR on {0}/{1}/{2}*
*Wells Monitored*
{3}
*TPR:*
{4}
*Remarks:*
{5}*Wellhead pressure:*
{6}
Regards
Gairik Das""".format(abc.day, abc.month, abc.year, total_wells_monitored, tpr_total, remarks_print,pressures)
        

class DPR():
    
    def __init__(self):
        
        #self.username= username
        return None

    
    def predict(self):
        with open('compiled.txt', 'w') as f:
            f.write(final)        
        return(None)  
        
model_load = DPR()
model_load.predict()