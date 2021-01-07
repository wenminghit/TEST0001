#coding=utf-8
#modbusRTU读取功能
#调用方法-01功能码，读取000地址
#mod_slave1_read2,mod_slave1_read2_sta=A.modbus_RTUmasterRead.main("com20",9600,8,'N',1,0,1,1,0,4)#串口,波特率,数据位,校验,停止位,控制位,站号,功能码,起始地址,地址长度
#调用方法-02功能码，读取1000地址
#mod_slave1_read2,mod_slave1_read2_sta=A.modbus_RTUmasterRead.main("com20",9600,8,'N',1,0,1,2,0,4)#串口,波特率,数据位,校验,停止位,控制位,站号,功能码,起始地址,地址长度
#调用方法-03功能码，读取4000地址
#mod_slave1_read1,mod_slave1_read1_sta=A.modbus_RTUmasterRead.main("com20",9600,8,'N',1,0,1,3,0,2)#串口,波特率,数据位,校验,停止位,控制位,站号,功能码,起始地址,地址长度
#调用方法-04功能码，读取3000地址
#mod_slave1_read1,mod_slave1_read1_sta=A.modbus_RTUmasterRead.main("com20",9600,8,'N',1,0,1,4,0,2)#串口,波特率,数据位,校验,停止位,控制位,站号,功能码,起始地址,地址长度
#调用参数设定("COM20",9600,8,"N",1,0,2,4,0,14)#串口,波特率,数据位,校验,停止位,控制位,站号,功能码,起始地址,地址长度
def main(INport,INbaudrate,INbytesize,INparity,INstopbits,INxonxoff,ID,Func,start_data,data_len):
    #import module
    import serial
    import modbus_tk
    import modbus_tk.defines as cst
    from modbus_tk import modbus_rtu
    read = []
    alarm = ""
    try:
        master = modbus_rtu.RtuMaster(serial.Serial(port=INport, baudrate=INbaudrate, bytesize=INbytesize, parity=INparity, stopbits=INstopbits, xonxoff=INxonxoff))
        master.set_timeout(5.0)#
        master.set_verbose(True)
        alarm = "正常"
        if Func==1:#读线圈寄存器
            read=master.execute(ID,cst.READ_COILS,start_data, data_len)
        elif Func==2:#读离散输入寄存器
            read=master.execute(ID,cst.READ_DISCRETE_INPUTS, start_data, data_len)
        elif Func==3:#读保持寄存器
            read=master.execute(ID,cst.READ_HOLDING_REGISTERS,start_data,data_len)
        elif Func==4:#读输入寄存器
            read=master.execute(ID,cst.READ_INPUT_REGISTERS, start_data, data_len) 
        else:
            print("功能码错误")
        return list(read),alarm
    except Exception as exc:
        #print(str(exc))
        alarm = (str(exc))
        return read, alarm  ##如果异常就返回[],故障信息
    else:
        pass
    finally:
        pass
if __name__ == "__main__":
    main()


