# Time Entry

> td = 4 : 代表羽 1
> tr 從 2 開始依序
> 1 個時段 6 個廠 (永和)
> 6-22

* 6-7
    * 羽 1 //tbody/tr[2]/td[4]/img[1]
    * 羽 2 //tbody/tr[3]/td[3]/img[1]
* 7-8
    * 羽 1 //tbody/tr[8]/td[4]/img[1]
    * //tbody/tr[3]/td[3]/img[1]
    * //tbody/tr[10]/td[3]/img[1]

## Bug
```bash
Exception in thread Thread-1:
Traceback (most recent call last):
  File "C:\Users\user\anaconda3\lib\threading.py", line 932, in _bootstrap_inner
    self.run()
  File "d:\autobooking_Copy\Center\JhongJhengSportsCenter.py", line 13, in run
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\JhongJhengState\LoginState.py", line 34, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\JhongJhengState\MainPageState.py", line 16, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\JhongJhengState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\JhongJhengState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\JhongJhengState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\JhongJhengState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\JhongJhengState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\JhongJhengState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\JhongJhengState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\JhongJhengState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\JhongJhengState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\JhongJhengState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\JhongJhengState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\JhongJhengState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\JhongJhengState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\JhongJhengState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\JhongJhengState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\JhongJhengState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\JhongJhengState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\JhongJhengState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\JhongJhengState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\JhongJhengState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\JhongJhengState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\JhongJhengState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\JhongJhengState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\JhongJhengState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\JhongJhengState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\JhongJhengState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\JhongJhengState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\JhongJhengState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\JhongJhengState\SelectPeriod.py", line 14, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\JhongJhengState\CalculateEmptyCourtsState.py", line 43, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\JhongJhengState\PickCourtState.py", line 10, in handle
    courts = center.targetCourts[center.orderNum]
AttributeError: 'JhongJhengSportCenter' object has no attribute 'targetCourts'
Exception in thread Thread-2:
Traceback (most recent call last):
  File "C:\Users\user\anaconda3\lib\threading.py", line 932, in _bootstrap_inner
    self.run()
  File "d:\autobooking_Copy\Center\YongHeSportsCenter.py", line 13, in run
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\YongHeState\LoginState.py", line 33, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\YongHeState\MainPageState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\YongHeState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\YongHeState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\YongHeState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\YongHeState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\YongHeState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\YongHeState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\YongHeState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\YongHeState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\YongHeState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\YongHeState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\YongHeState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\YongHeState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\YongHeState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\YongHeState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\YongHeState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\YongHeState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\YongHeState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\YongHeState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\YongHeState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\YongHeState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\YongHeState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\YongHeState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\YongHeState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\YongHeState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\YongHeState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\YongHeState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\YongHeState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\YongHeState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\YongHeState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\YongHeState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\YongHeState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\YongHeState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\YongHeState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\YongHeState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\YongHeState\SelectPeriod.py", line 18, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\YongHeState\CalculateEmptyCourtsState.py", line 47, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\YongHeState\PickCourtState.py", line 25, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\YongHeState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\YongHeState\SelectPeriod.py", line 18, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\YongHeState\PickCourtState.py", line 18, in handle
    alert.accept()
  File "C:\Users\user\anaconda3\lib\site-packages\selenium\webdriver\common\alert.py", line 81, in accept
    self.driver.execute(Command.W3C_ACCEPT_ALERT)
  File "C:\Users\user\anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 418, in execute
    self.error_handler.check_response(response)
  File "C:\Users\user\anaconda3\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 243, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoAlertPresentException: Message: no such alert
  (Session info: chrome=106.0.5249.119)
Stacktrace:
Backtrace:
        Ordinal0 [0x00541ED3+2236115]
        Ordinal0 [0x004D92F1+1807089]
        Ordinal0 [0x003E65C0+812480]
        Ordinal0 [0x003DF7DB+784347]
        Ordinal0 [0x003F8D01+888065]
        Ordinal0 [0x00431B04+1121028]
        Ordinal0 [0x003F8742+886594]
        Ordinal0 [0x004318A6+1120422]
        Ordinal0 [0x0040A73D+960317]
        Ordinal0 [0x0040B71F+964383]
        GetHandleVerifier [0x007EE7E2+2743074]
        GetHandleVerifier [0x007E08D4+2685972]
        GetHandleVerifier [0x005D2BAA+532202]
        GetHandleVerifier [0x005D1990+527568]
        Ordinal0 [0x004E080C+1837068]
        Ordinal0 [0x004E4CD8+1854680]
        Ordinal0 [0x004E4DC5+1854917]
        Ordinal0 [0x004EED64+1895780]
        BaseThreadInitThunk [0x76C4FA29+25]
        RtlGetAppContainerNamedObjectPath [0x77B07BBE+286]
        RtlGetAppContainerNamedObjectPath [0x77B07B8E+238]
```