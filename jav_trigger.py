import subprocess
import json
def jar_trigger(numplate):
    # sub = subprocess.call(['java', '-jar', 'Validate.jar', 'MH12DE1433'])
    sub=subprocess.run(['java', '-jar', 'Validate.jar', numplate],capture_output=True,text=True)
    sub1=sub.stdout
    # print('sub',sub1)
    # print(type(sub1))
    if "Error" in sub1:
        return (False,'')

    sub_dict=json.loads(sub1)
    # print(sub_dict["Vehicle Class"])
    return(True,sub_dict["Vehicle Class"])
if __name__=='__main__':
    jar_trigger('UP16AT8647')