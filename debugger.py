"""
BOOL WINAPI CreateProcess(
  _In_opt_    LPCTSTR               lpApplicationName,
  _Inout_opt_ LPTSTR                lpCommandLine,
  _In_opt_    LPSECURITY_ATTRIBUTES lpProcessAttributes,
  _In_opt_    LPSECURITY_ATTRIBUTES lpThreadAttributes,
  _In_        BOOL                  bInheritHandles,
  _In_        DWORD                 dwCreationFlags,
  _In_opt_    LPVOID                lpEnvironment,
  _In_opt_    LPCTSTR               lpCurrentDirectory,
  _In_        LPSTARTUPINFO         lpStartupInfo,
  _Out_       LPPROCESS_INFORMATION lpProcessInformation
);
"""
from ctypes import *
from debugger_defines import *

kernel32= windll.kernel32

class debugger():
  def _init_(self):
    pass

  def load(self,pathExec):
    creationFlags = DEBUG_PROCESS

    #instantiate structs
    startupInfo = STARTUPINFO();
    processInformation = PROCESS_INFORMATION();

    startupInfo.dwFlags = 0x1
    startupInfo.wShowWindow = 0x0

    startupInfo.cp=sizeof(startupInfo)


    if kernel32.CreateProcessA(path_to_exe,
                                  None,
                                  None,
                                  None,
                                  None,
                                  creation_flags,
                                  None,
                                  None,
                                  byref(startupinfo),
                                  byref(process_information)):
        print "[*] We have successfully launched the process!"
        print "[*] PID: %d" % process_information.dwProcessId

            # Obtain a valid handle to the newly created process
            # and store it for future access
        self.h_process = self.open_process(process_information.dwProcessId)
        print self.h_process

    else:
        print "[*] Error: 0x%08x." % kernel32.GetLastError()
