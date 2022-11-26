import Center.BanQiaoSportsCenter as BanQiao
import Center.DaAnSportsCenter as DaAn
import Center.JhongJhengSportsCenter as JhongJheng
import Center.LinKouSportsCenter as LinKou
import Center.NanGangSportsCenter as NanGang
import Center.YongHeSportsCenter as YongHe
import Center.ZhugUangSportsCenter as ZhugUang
import SportsCenterState.LoginState as Login

class CenterFactory:
    @staticmethod
    def createCenter(time, type):
        if (type == 'BanQiao'):
            return BanQiao.BanQiaoSportsCenter(time), Login.LoginState()
        elif(type == 'DaAn'):
            return DaAn.DaAnSportsCenter(time), Login.LoginState()
        elif(type == 'JhongJheng'):
            return JhongJheng.JhongJhengSportsCenter(time), Login.LoginState()
        elif(type == 'LinKou'):
            return LinKou.LinKouSportsCenter(time), Login.LoginState()
        elif(type == 'NanGang'):
            return NanGang.NanGangSportsCenter(time), Login.LoginState()
        elif(type == 'YongHe'):
            return YongHe.YongHeSportsCenter(time), Login.LoginState()
        elif(type == 'ZhugUang'):
            return ZhugUang.ZhugUangSportsCenter(time), Login.LoginState()
        else:
            raise BaseException("No Such Center")