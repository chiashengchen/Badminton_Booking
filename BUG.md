# BUG

## 11/19

### YongHeSportsCenter

```bash
Traceback (most recent call last):
  File "C:\Users\user\anaconda3\lib\threading.py", line 932, in _bootstrap_inner
    self.run()
  File "d:\autobooking_Copy\Center\YongHeSportsCenter.py", line 24, in run
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\YongHeState\LoginState.py", line 34, in handle
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
  File "d:\autobooking_Copy\SportsCenterState\YongHeState\SelectPeriod.py", line 18, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\YongHeState\CalculateEmptyCourtsState.py", line 48, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\YongHeState\PickCourtState.py", line 27, in handle
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
  File "d:\autobooking_Copy\SportsCenterState\YongHeState\PickCourtState.py", line 27, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
TypeError: handle() missing 1 required positional argument: 'center'
Exception in thread Thread-5:
```
### BanQiaoSportsCenter
```bash
Exception in thread Thread-1:
Traceback (most recent call last):
  File "C:\Users\user\anaconda3\lib\threading.py", line 932, in _bootstrap_inner
    self.run()
  File "d:\autobooking_Copy\Center\BanQiaoSportsCenter.py", line 25, in run
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\BanQiaoState\LoginState.py", line 33, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\BanQiaoState\MainPageState.py", line 16, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\BanQiaoState\SelectDayState.py", line 14, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\BanQiaoState\SelectPeriod.py", line 14, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\BanQiaoState\CalculateEmptyCourtsState.py", line 49, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\BanQiaoState\PickCourtState.py", line 13, in handle
    if "alert" in center.driver.find_element(By.XPATH, court).get_attribute("onclick"):
  File "C:\Users\user\anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 1238, in find_element
    return self.execute(Command.FIND_ELEMENT, {
  File "C:\Users\user\anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 418, in execute
    self.error_handler.check_response(response)
  File "C:\Users\user\anaconda3\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 243, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"xpath","selector":"//tbody/tr[25]/td[4]/img[1]"}
  (Session info: chrome=107.0.5304.107)
Stacktrace:
Backtrace:
        Ordinal0 [0x00581ED3+2236115]
        Ordinal0 [0x005192F1+1807089]
        Ordinal0 [0x004266FD+812797]
        Ordinal0 [0x004555DF+1005023]
        Ordinal0 [0x004557CB+1005515]
        Ordinal0 [0x00487632+1209906]
        Ordinal0 [0x00471AD4+1120980]
        Ordinal0 [0x004859E2+1202658]
        Ordinal0 [0x004718A6+1120422]
        Ordinal0 [0x0044A73D+960317]
        Ordinal0 [0x0044B71F+964383]
        GetHandleVerifier [0x0082E7E2+2743074]
        GetHandleVerifier [0x008208D4+2685972]
        GetHandleVerifier [0x00612BAA+532202]
        GetHandleVerifier [0x00611990+527568]
        Ordinal0 [0x0052080C+1837068]
        Ordinal0 [0x00524CD8+1854680]
        Ordinal0 [0x00524DC5+1854917]
        Ordinal0 [0x0052ED64+1895780]
        BaseThreadInitThunk [0x7668FEF9+25]
        RtlGetAppContainerNamedObjectPath [0x77107BBE+286]
        RtlGetAppContainerNamedObjectPath [0x77107B8E+238]

```
### LinKouSportsCenter
```bash

[9780:7352:1119/160020.445:ERROR:util.cc(129)] Can't create base directory: C:\Program Files\Google\GoogleUpdater
[6296:11636:1119/160022.112:ERROR:util.cc(129)] Can't create base directory: C:\Program Files\Google\GoogleUpdater
[7072:11940:1119/160113.630:ERROR:gpu_init.cc(537)] Passthrough is not supported, GL is disabled, ANGLE is 
[13016:13012:1119/160115.423:ERROR:gpu_init.cc(537)] Passthrough is not supported, GL is disabled, ANGLE is 
[8448:8444:1119/160117.158:ERROR:gpu_init.cc(537)] Passthrough is not supported, GL is disabled, ANGLE is 
[3404:3140:1119/160118.880:ERROR:gpu_init.cc(537)] Passthrough is not supported, GL is disabled, ANGLE is 
[12940:8912:1119/160120.533:ERROR:gpu_init.cc(537)] Passthrough is not supported, GL is disabled, ANGLE is 
[13060:5948:1119/160122.199:ERROR:gpu_init.cc(537)] Passthrough is not supported, GL is disabled, ANGLE is 
Order 1 in Da An
Not enough courts !!
Order 1 in Lin Kou
Order 1 in Yong He
Order 2 in Yong He
Exception in thread Thread-3:


Order 2 in Lin Kou
Exception in thread Thread-6:
Traceback (most recent call last):
  File "C:\Users\user\anaconda3\lib\threading.py", line 932, in _bootstrap_inner
    self.run()
  File "d:\autobooking_Copy\Center\LinKouSportsCenter.py", line 25, in run
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\LinKouState\LoginState.py", line 34, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\LinKouState\MainPageState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\LinKouState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\LinKouState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\LinKouState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\LinKouState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\LinKouState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\LinKouState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\LinKouState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\LinKouState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\LinKouState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\LinKouState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\LinKouState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\LinKouState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\LinKouState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\LinKouState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\LinKouState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\LinKouState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\LinKouState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\LinKouState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\LinKouState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\LinKouState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\LinKouState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\LinKouState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\LinKouState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\LinKouState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\LinKouState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\LinKouState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\LinKouState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\LinKouState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\LinKouState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\LinKouState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\LinKouState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\LinKouState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\LinKouState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\LinKouState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\LinKouState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\LinKouState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\LinKouState\SelectPeriod.py", line 18, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\LinKouState\CalculateEmptyCourtsState.py", line 48, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\LinKouState\PickCourtState.py", line 27, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\LinKouState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\LinKouState\SelectPeriod.py", line 18, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handlenter.py", line 28, in handle
    self.state.handle(self)                  \LinKouState\PickCourtState.py", line 27, in handle
  File "d:\autobooking_Copy\SportsCenterStatete\LinKouState\PickCourtState.py", line 27,n er.py", line 28, in handle in handle
    center.handle()                          onal argument: 'center'
  File "d:\autobooking_Copy\Center\SportsCentnter.py", line 28, in handle
    self.state.handle(self)
TypeError: handle() missing 1 required posititional argument: 'center'
```
### DaAnSportsCenter
```bash
Traceback (most recent call last):
  File "C:\Users\user\anaconda3\lib\threading.py", line 932, in _bootstrap_inner
    self.run()
  File "d:\autobooking_Copy\Center\DaAnSportsCenter.py", line 27, in run
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\DaAnState\LoginState.py", line 33, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\DaAnState\LoginState.py", line 33, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\DaAnState\MainPageState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\DaAnState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\DaAnState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\DaAnState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\DaAnState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\DaAnState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\DaAnState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\DaAnState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\DaAnState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\DaAnState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\DaAnState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\DaAnState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\DaAnState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\DaAnState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\DaAnState\SelectPeriod.py", line 18, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\DaAnState\CalculateEmptyCourtsState.py", line 48, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\DaAnState\PickCourtState.py", line 27, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\DaAnState\SelectDayState.py", line 15, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\DaAnState\SelectPeriod.py", line 18, in handle
    center.handle()
  File "d:\autobooking_Copy\Center\SportsCenter.py", line 28, in handle
    self.state.handle(self)
  File "d:\autobooking_Copy\SportsCenterState\DaAnState\PickCourtState.py", line 25, in handle
    center.driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_Step3Info_lab"]/span[2]/a[3]').click()
  File "C:\Users\user\anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 1238, in find_element
    return self.execute(Command.FIND_ELEMENT, {
  File "C:\Users\user\anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 418, in execute
    self.error_handler.check_response(response)
  File "C:\Users\user\anaconda3\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 243, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"xpath","selector":"//*[@id="ContentPlaceHolder1_Step3Info_lab"]/span[2]/a[3]"}
  (Session info: chrome=107.0.5304.107)
Stacktrace:
Backtrace:
        Ordinal0 [0x00581ED3+2236115]
        Ordinal0 [0x005192F1+1807089]
        Ordinal0 [0x004266FD+812797]
        Ordinal0 [0x004555DF+1005023]
        Ordinal0 [0x004557CB+1005515]
        Ordinal0 [0x00487632+1209906]
        Ordinal0 [0x00471AD4+1120980]
        Ordinal0 [0x004859E2+1202658]
        Ordinal0 [0x004718A6+1120422]
        Ordinal0 [0x0044A73D+960317]
        Ordinal0 [0x0044B71F+964383]
        GetHandleVerifier [0x0082E7E2+2743074]
        GetHandleVerifier [0x008208D4+2685972]
        GetHandleVerifier [0x00612BAA+532202]
        GetHandleVerifier [0x00611990+527568]
        Ordinal0 [0x0052080C+1837068]
        Ordinal0 [0x00524CD8+1854680]
        Ordinal0 [0x00524DC5+1854917]
        Ordinal0 [0x0052ED64+1895780]
        BaseThreadInitThunk [0x7668FEF9+25]
        RtlGetAppContainerNamedObjectPath [0x77107BBE+286]
        RtlGetAppContainerNamedObjectPath [0x77107B8E+238]

```