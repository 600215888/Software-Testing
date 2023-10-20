# REPORT

## Personal Information
- Student Name: Hanzhe Zhang
- Student ID: 20887285
- WatID: h843zhan

## What have been done to compile and run the code
I first download docker on my laptop, which allows me to run fuzz on my windows basied laptop. I also created a container by using docker.
Then I follow the video tutorial step by step, and successfully get a really basic coverage.

## What have been done to increase the coverage
I first used freedoom2.wad as my corpus to run the command, then I get a basic coverage. 
After generating the report, I realized that w_wad.c is about 70%, which is lower than the standard of excellent. 
One problem I want to improve is about filename begins with '~', so I create fuzz_target1.c and change filename to a string starts with a '~'to cover it.
After that, I want to cover that part where filename ends with 'wad'. This is really complex, to solve this, I changed w_file.c and make its return value is always true.
After doing that, I createde a file called 'z.zad' whose last three char is bigger than 'wad'. 
Then I created fuzz_target2.c, and covered that part.
After doing all the work, I find it is hard for me to add all the 3 fuzz_target files as one excutable, so I had to cmake and fuzzed my project for my 3 fuzz_target files, respectively, and merge 3 pf-* files to get excellent grades. 

## What bugs have been found? Can you replay the bug with chocolate-doom, not with the fuzz target?
==31242==ERROR: LeakSanitizer: detected memory leaks

Direct leak of 136 byte(s) in 10 object(s) allocated from:
    #0 0x434974 in strdup (/home/doom/stqam/fb/build7/src/doom_fuzz+0x434974)
    #1 0x4dc160 in M_StringDuplicate /home/doom/stqam/fb/build7/../chocolate-doom/src/m_misc.c:423:14
    #2 0x4ecbe0 in D_BindVariables /home/doom/stqam/fb/build7/../chocolate-doom/src/doom/d_main.c:382:26
    #3 0x477f02 in LLVMFuzzerTestOneInput /home/doom/stqam/fb/build7/../src/fuzz_target.c:166:3
    #4 0x382a71 in fuzzer::Fuzzer::ExecuteCallback(unsigned char const*, unsigned long) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x382a71)
    #5 0x3821b5 in fuzzer::Fuzzer::RunOne(unsigned char const*, unsigned long, bool, fuzzer::InputInfo*, bool*) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x3821b5)
    #6 0x384991 in fuzzer::Fuzzer::ReadAndExecuteSeedCorpora(std::__Fuzzer::vector<fuzzer::SizedFile, fuzzer::fuzzer_allocator<fuzzer::SizedFile> >&) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x384991)
    #7 0x384e39 in fuzzer::Fuzzer::Loop(std::__Fuzzer::vector<fuzzer::SizedFile, fuzzer::fuzzer_allocator<fuzzer::SizedFile> >&) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x384e39)
    #8 0x372ebe in fuzzer::FuzzerDriver(int*, char***, int (*)(unsigned char const*, unsigned long)) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x372ebe)
    #9 0x39c952 in main (/home/doom/stqam/fb/build7/src/doom_fuzz+0x39c952)
    #10 0x7fcbd75abbf6 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21bf6)

Direct leak of 136 byte(s) in 10 object(s) allocated from:
    #0 0x434974 in strdup (/home/doom/stqam/fb/build7/src/doom_fuzz+0x434974)
    #1 0x4dc160 in M_StringDuplicate /home/doom/stqam/fb/build7/../chocolate-doom/src/m_misc.c:423:14
    #2 0x4a11a4 in SetVariable /home/doom/stqam/fb/build7/../chocolate-doom/src/m_config.c:1942:32
    #3 0x4a05f2 in LoadDefaultCollection /home/doom/stqam/fb/build7/../chocolate-doom/src/m_config.c:2031:9
    #4 0x49fce5 in M_LoadDefaults /home/doom/stqam/fb/build7/../chocolate-doom/src/m_config.c:2137:5
    #5 0x477f07 in LLVMFuzzerTestOneInput /home/doom/stqam/fb/build7/../src/fuzz_target.c:167:3
    #6 0x382a71 in fuzzer::Fuzzer::ExecuteCallback(unsigned char const*, unsigned long) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x382a71)
    #7 0x3821b5 in fuzzer::Fuzzer::RunOne(unsigned char const*, unsigned long, bool, fuzzer::InputInfo*, bool*) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x3821b5)
    #8 0x384457 in fuzzer::Fuzzer::MutateAndTestOne() (/home/doom/stqam/fb/build7/src/doom_fuzz+0x384457)
    #9 0x385155 in fuzzer::Fuzzer::Loop(std::__Fuzzer::vector<fuzzer::SizedFile, fuzzer::fuzzer_allocator<fuzzer::SizedFile> >&) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x385155)
    #10 0x372ebe in fuzzer::FuzzerDriver(int*, char***, int (*)(unsigned char const*, unsigned long)) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x372ebe)
    #11 0x39c952 in main (/home/doom/stqam/fb/build7/src/doom_fuzz+0x39c952)
    #12 0x7fcbd75abbf6 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21bf6)

Direct leak of 136 byte(s) in 10 object(s) allocated from:
    #0 0x434974 in strdup (/home/doom/stqam/fb/build7/src/doom_fuzz+0x434974)
    #1 0x4dc160 in M_StringDuplicate /home/doom/stqam/fb/build7/../chocolate-doom/src/m_misc.c:423:14
    #2 0x4a11a4 in SetVariable /home/doom/stqam/fb/build7/../chocolate-doom/src/m_config.c:1942:32
    #3 0x4a05f2 in LoadDefaultCollection /home/doom/stqam/fb/build7/../chocolate-doom/src/m_config.c:2031:9
    #4 0x49fce5 in M_LoadDefaults /home/doom/stqam/fb/build7/../chocolate-doom/src/m_config.c:2137:5
    #5 0x477f07 in LLVMFuzzerTestOneInput /home/doom/stqam/fb/build7/../src/fuzz_target.c:167:3
    #6 0x382a71 in fuzzer::Fuzzer::ExecuteCallback(unsigned char const*, unsigned long) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x382a71)
    #7 0x3821b5 in fuzzer::Fuzzer::RunOne(unsigned char const*, unsigned long, bool, fuzzer::InputInfo*, bool*) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x3821b5)
    #8 0x384991 in fuzzer::Fuzzer::ReadAndExecuteSeedCorpora(std::__Fuzzer::vector<fuzzer::SizedFile, fuzzer::fuzzer_allocator<fuzzer::SizedFile> >&) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x384991)
    #9 0x384e39 in fuzzer::Fuzzer::Loop(std::__Fuzzer::vector<fuzzer::SizedFile, fuzzer::fuzzer_allocator<fuzzer::SizedFile> >&) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x384e39)
    #10 0x372ebe in fuzzer::FuzzerDriver(int*, char***, int (*)(unsigned char const*, unsigned long)) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x372ebe)
    #11 0x39c952 in main (/home/doom/stqam/fb/build7/src/doom_fuzz+0x39c952)
    #12 0x7fcbd75abbf6 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21bf6)

Direct leak of 136 byte(s) in 10 object(s) allocated from:
    #0 0x434974 in strdup (/home/doom/stqam/fb/build7/src/doom_fuzz+0x434974)
    #1 0x4dc160 in M_StringDuplicate /home/doom/stqam/fb/build7/../chocolate-doom/src/m_misc.c:423:14
    #2 0x4a11a4 in SetVariable /home/doom/stqam/fb/build7/../chocolate-doom/src/m_config.c:1942:32
    #3 0x4a05f2 in LoadDefaultCollection /home/doom/stqam/fb/build7/../chocolate-doom/src/m_config.c:2031:9
    #4 0x49fce5 in M_LoadDefaults /home/doom/stqam/fb/build7/../chocolate-doom/src/m_config.c:2137:5
    #5 0x477f07 in LLVMFuzzerTestOneInput /home/doom/stqam/fb/build7/../src/fuzz_target.c:167:3
    #6 0x382a71 in fuzzer::Fuzzer::ExecuteCallback(unsigned char const*, unsigned long) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x382a71)
    #7 0x3847aa in fuzzer::Fuzzer::ReadAndExecuteSeedCorpora(std::__Fuzzer::vector<fuzzer::SizedFile, fuzzer::fuzzer_allocator<fuzzer::SizedFile> >&) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x3847aa)
    #8 0x384e39 in fuzzer::Fuzzer::Loop(std::__Fuzzer::vector<fuzzer::SizedFile, fuzzer::fuzzer_allocator<fuzzer::SizedFile> >&) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x384e39)
    #9 0x372ebe in fuzzer::FuzzerDriver(int*, char***, int (*)(unsigned char const*, unsigned long)) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x372ebe)
    #10 0x39c952 in main (/home/doom/stqam/fb/build7/src/doom_fuzz+0x39c952)
    #11 0x7fcbd75abbf6 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21bf6)

Direct leak of 136 byte(s) in 10 object(s) allocated from:
    #0 0x434974 in strdup (/home/doom/stqam/fb/build7/src/doom_fuzz+0x434974)
    #1 0x4dc160 in M_StringDuplicate /home/doom/stqam/fb/build7/../chocolate-doom/src/m_misc.c:423:14
    #2 0x4ecbe0 in D_BindVariables /home/doom/stqam/fb/build7/../chocolate-doom/src/doom/d_main.c:382:26
    #3 0x477f02 in LLVMFuzzerTestOneInput /home/doom/stqam/fb/build7/../src/fuzz_target.c:166:3
    #4 0x382a71 in fuzzer::Fuzzer::ExecuteCallback(unsigned char const*, unsigned long) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x382a71)
    #5 0x3847aa in fuzzer::Fuzzer::ReadAndExecuteSeedCorpora(std::__Fuzzer::vector<fuzzer::SizedFile, fuzzer::fuzzer_allocator<fuzzer::SizedFile> >&) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x3847aa)
    #6 0x384e39 in fuzzer::Fuzzer::Loop(std::__Fuzzer::vector<fuzzer::SizedFile, fuzzer::fuzzer_allocator<fuzzer::SizedFile> >&) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x384e39)
    #7 0x372ebe in fuzzer::FuzzerDriver(int*, char***, int (*)(unsigned char const*, unsigned long)) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x372ebe)
    #8 0x39c952 in main (/home/doom/stqam/fb/build7/src/doom_fuzz+0x39c952)
    #9 0x7fcbd75abbf6 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21bf6)

Direct leak of 136 byte(s) in 10 object(s) allocated from:
    #0 0x434974 in strdup (/home/doom/stqam/fb/build7/src/doom_fuzz+0x434974)
    #1 0x4dc160 in M_StringDuplicate /home/doom/stqam/fb/build7/../chocolate-doom/src/m_misc.c:423:14
    #2 0x4ecbe0 in D_BindVariables /home/doom/stqam/fb/build7/../chocolate-doom/src/doom/d_main.c:382:26
    #3 0x477f02 in LLVMFuzzerTestOneInput /home/doom/stqam/fb/build7/../src/fuzz_target.c:166:3
    #4 0x382a71 in fuzzer::Fuzzer::ExecuteCallback(unsigned char const*, unsigned long) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x382a71)
    #5 0x3821b5 in fuzzer::Fuzzer::RunOne(unsigned char const*, unsigned long, bool, fuzzer::InputInfo*, bool*) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x3821b5)
    #6 0x384457 in fuzzer::Fuzzer::MutateAndTestOne() (/home/doom/stqam/fb/build7/src/doom_fuzz+0x384457)
    #7 0x385155 in fuzzer::Fuzzer::Loop(std::__Fuzzer::vector<fuzzer::SizedFile, fuzzer::fuzzer_allocator<fuzzer::SizedFile> >&) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x385155)
    #8 0x372ebe in fuzzer::FuzzerDriver(int*, char***, int (*)(unsigned char const*, unsigned long)) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x372ebe)
    #9 0x39c952 in main (/home/doom/stqam/fb/build7/src/doom_fuzz+0x39c952)
    #10 0x7fcbd75abbf6 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21bf6)

Direct leak of 72 byte(s) in 10 object(s) allocated from:
    #0 0x434974 in strdup (/home/doom/stqam/fb/build7/src/doom_fuzz+0x434974)
    #1 0x4dc160 in M_StringDuplicate /home/doom/stqam/fb/build7/../chocolate-doom/src/m_misc.c:423:14
    #2 0x4a11a4 in SetVariable /home/doom/stqam/fb/build7/../chocolate-doom/src/m_config.c:1942:32
    #3 0x4a05f2 in LoadDefaultCollection /home/doom/stqam/fb/build7/../chocolate-doom/src/m_config.c:2031:9
    #4 0x477f07 in LLVMFuzzerTestOneInput /home/doom/stqam/fb/build7/../src/fuzz_target.c:167:3
    #5 0x382a71 in fuzzer::Fuzzer::ExecuteCallback(unsigned char const*, unsigned long) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x382a71)
    #6 0x3821b5 in fuzzer::Fuzzer::RunOne(unsigned char const*, unsigned long, bool, fuzzer::InputInfo*, bool*) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x3821b5)
    #7 0x384991 in fuzzer::Fuzzer::ReadAndExecuteSeedCorpora(std::__Fuzzer::vector<fuzzer::SizedFile, fuzzer::fuzzer_allocator<fuzzer::SizedFile> >&) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x384991)
    #8 0x384e39 in fuzzer::Fuzzer::Loop(std::__Fuzzer::vector<fuzzer::SizedFile, fuzzer::fuzzer_allocator<fuzzer::SizedFile> >&) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x384e39)
    #9 0x372ebe in fuzzer::FuzzerDriver(int*, char***, int (*)(unsigned char const*, unsigned long)) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x372ebe)
    #10 0x39c952 in main (/home/doom/stqam/fb/build7/src/doom_fuzz+0x39c952)
    #11 0x7fcbd75abbf6 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21bf6)

Direct leak of 72 byte(s) in 10 object(s) allocated from:
    #0 0x434974 in strdup (/home/doom/stqam/fb/build7/src/doom_fuzz+0x434974)
    #1 0x4dc160 in M_StringDuplicate /home/doom/stqam/fb/build7/../chocolate-doom/src/m_misc.c:423:14
    #2 0x4a11a4 in SetVariable /home/doom/stqam/fb/build7/../chocolate-doom/src/m_config.c:1942:32
    #3 0x4a05f2 in LoadDefaultCollection /home/doom/stqam/fb/build7/../chocolate-doom/src/m_config.c:2031:9
    #4 0x477f07 in LLVMFuzzerTestOneInput /home/doom/stqam/fb/build7/../src/fuzz_target.c:167:3
    #5 0x382a71 in fuzzer::Fuzzer::ExecuteCallback(unsigned char const*, unsigned long) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x382a71)
    #6 0x3821b5 in fuzzer::Fuzzer::RunOne(unsigned char const*, unsigned long, bool, fuzzer::InputInfo*, bool*) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x3821b5)
    #7 0x384457 in fuzzer::Fuzzer::MutateAndTestOne() (/home/doom/stqam/fb/build7/src/doom_fuzz+0x384457)
    #8 0x385155 in fuzzer::Fuzzer::Loop(std::__Fuzzer::vector<fuzzer::SizedFile, fuzzer::fuzzer_allocator<fuzzer::SizedFile> >&) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x385155)
    #9 0x372ebe in fuzzer::FuzzerDriver(int*, char***, int (*)(unsigned char const*, unsigned long)) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x372ebe)
    #10 0x39c952 in main (/home/doom/stqam/fb/build7/src/doom_fuzz+0x39c952)
    #11 0x7fcbd75abbf6 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21bf6)

Direct leak of 72 byte(s) in 10 object(s) allocated from:
    #0 0x434974 in strdup (/home/doom/stqam/fb/build7/src/doom_fuzz+0x434974)
    #1 0x4dc160 in M_StringDuplicate /home/doom/stqam/fb/build7/../chocolate-doom/src/m_misc.c:423:14
    #2 0x4a11a4 in SetVariable /home/doom/stqam/fb/build7/../chocolate-doom/src/m_config.c:1942:32
    #3 0x4a05f2 in LoadDefaultCollection /home/doom/stqam/fb/build7/../chocolate-doom/src/m_config.c:2031:9
    #4 0x477f07 in LLVMFuzzerTestOneInput /home/doom/stqam/fb/build7/../src/fuzz_target.c:167:3
    #5 0x382a71 in fuzzer::Fuzzer::ExecuteCallback(unsigned char const*, unsigned long) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x382a71)
    #6 0x3847aa in fuzzer::Fuzzer::ReadAndExecuteSeedCorpora(std::__Fuzzer::vector<fuzzer::SizedFile, fuzzer::fuzzer_allocator<fuzzer::SizedFile> >&) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x3847aa)
    #7 0x384e39 in fuzzer::Fuzzer::Loop(std::__Fuzzer::vector<fuzzer::SizedFile, fuzzer::fuzzer_allocator<fuzzer::SizedFile> >&) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x384e39)
    #8 0x372ebe in fuzzer::FuzzerDriver(int*, char***, int (*)(unsigned char const*, unsigned long)) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x372ebe)
    #9 0x39c952 in main (/home/doom/stqam/fb/build7/src/doom_fuzz+0x39c952)
    #10 0x7fcbd75abbf6 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21bf6)

Direct leak of 58 byte(s) in 1 object(s) allocated from:
    #0 0x4485cd in malloc (/home/doom/stqam/fb/build7/src/doom_fuzz+0x4485cd)
    #1 0x4dca23 in M_StringJoin /home/doom/stqam/fb/build7/../chocolate-doom/src/m_misc.c:575:14
    #2 0x49fcd4 in M_LoadDefaults /home/doom/stqam/fb/build7/../chocolate-doom/src/m_config.c:2134:15
    #3 0x477f07 in LLVMFuzzerTestOneInput /home/doom/stqam/fb/build7/../src/fuzz_target.c:167:3
    #4 0x382a71 in fuzzer::Fuzzer::ExecuteCallback(unsigned char const*, unsigned long) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x382a71)
    #5 0x3847aa in fuzzer::Fuzzer::ReadAndExecuteSeedCorpora(std::__Fuzzer::vector<fuzzer::SizedFile, fuzzer::fuzzer_allocator<fuzzer::SizedFile> >&) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x3847aa)
    #6 0x384e39 in fuzzer::Fuzzer::Loop(std::__Fuzzer::vector<fuzzer::SizedFile, fuzzer::fuzzer_allocator<fuzzer::SizedFile> >&) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x384e39)
    #7 0x372ebe in fuzzer::FuzzerDriver(int*, char***, int (*)(unsigned char const*, unsigned long)) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x372ebe)
    #8 0x39c952 in main (/home/doom/stqam/fb/build7/src/doom_fuzz+0x39c952)
    #9 0x7fcbd75abbf6 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21bf6)

Direct leak of 58 byte(s) in 1 object(s) allocated from:
    #0 0x4485cd in malloc (/home/doom/stqam/fb/build7/src/doom_fuzz+0x4485cd)
    #1 0x4dca23 in M_StringJoin /home/doom/stqam/fb/build7/../chocolate-doom/src/m_misc.c:575:14
    #2 0x49fcd4 in M_LoadDefaults /home/doom/stqam/fb/build7/../chocolate-doom/src/m_config.c:2134:15
    #3 0x477f07 in LLVMFuzzerTestOneInput /home/doom/stqam/fb/build7/../src/fuzz_target.c:167:3
    #4 0x382a71 in fuzzer::Fuzzer::ExecuteCallback(unsigned char const*, unsigned long) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x382a71)
    #5 0x3821b5 in fuzzer::Fuzzer::RunOne(unsigned char const*, unsigned long, bool, fuzzer::InputInfo*, bool*) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x3821b5)
    #6 0x384457 in fuzzer::Fuzzer::MutateAndTestOne() (/home/doom/stqam/fb/build7/src/doom_fuzz+0x384457)
    #7 0x385155 in fuzzer::Fuzzer::Loop(std::__Fuzzer::vector<fuzzer::SizedFile, fuzzer::fuzzer_allocator<fuzzer::SizedFile> >&) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x385155)
    #8 0x372ebe in fuzzer::FuzzerDriver(int*, char***, int (*)(unsigned char const*, unsigned long)) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x372ebe)
    #9 0x39c952 in main (/home/doom/stqam/fb/build7/src/doom_fuzz+0x39c952)
    #10 0x7fcbd75abbf6 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21bf6)

Direct leak of 58 byte(s) in 1 object(s) allocated from:
    #0 0x4485cd in malloc (/home/doom/stqam/fb/build7/src/doom_fuzz+0x4485cd)
    #1 0x4dca23 in M_StringJoin /home/doom/stqam/fb/build7/../chocolate-doom/src/m_misc.c:575:14
    #2 0x49fcd4 in M_LoadDefaults /home/doom/stqam/fb/build7/../chocolate-doom/src/m_config.c:2134:15
    #3 0x477f07 in LLVMFuzzerTestOneInput /home/doom/stqam/fb/build7/../src/fuzz_target.c:167:3
    #4 0x382a71 in fuzzer::Fuzzer::ExecuteCallback(unsigned char const*, unsigned long) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x382a71)
    #5 0x3821b5 in fuzzer::Fuzzer::RunOne(unsigned char const*, unsigned long, bool, fuzzer::InputInfo*, bool*) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x3821b5)
    #6 0x384991 in fuzzer::Fuzzer::ReadAndExecuteSeedCorpora(std::__Fuzzer::vector<fuzzer::SizedFile, fuzzer::fuzzer_allocator<fuzzer::SizedFile> >&) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x384991)
    #7 0x384e39 in fuzzer::Fuzzer::Loop(std::__Fuzzer::vector<fuzzer::SizedFile, fuzzer::fuzzer_allocator<fuzzer::SizedFile> >&) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x384e39)
    #8 0x372ebe in fuzzer::FuzzerDriver(int*, char***, int (*)(unsigned char const*, unsigned long)) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x372ebe)
    #9 0x39c952 in main (/home/doom/stqam/fb/build7/src/doom_fuzz+0x39c952)
    #10 0x7fcbd75abbf6 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21bf6)

Direct leak of 51 byte(s) in 1 object(s) allocated from:
    #0 0x4485cd in malloc (/home/doom/stqam/fb/build7/src/doom_fuzz+0x4485cd)
    #1 0x4dca23 in M_StringJoin /home/doom/stqam/fb/build7/../chocolate-doom/src/m_misc.c:575:14
    #2 0x49fc09 in M_LoadDefaults /home/doom/stqam/fb/build7/../chocolate-doom/src/m_config.c:2111:15
    #3 0x477f07 in LLVMFuzzerTestOneInput /home/doom/stqam/fb/build7/../src/fuzz_target.c:167:3
    #4 0x382a71 in fuzzer::Fuzzer::ExecuteCallback(unsigned char const*, unsigned long) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x382a71)
    #5 0x3847aa in fuzzer::Fuzzer::ReadAndExecuteSeedCorpora(std::__Fuzzer::vector<fuzzer::SizedFile, fuzzer::fuzzer_allocator<fuzzer::SizedFile> >&) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x3847aa)
    #6 0x384e39 in fuzzer::Fuzzer::Loop(std::__Fuzzer::vector<fuzzer::SizedFile, fuzzer::fuzzer_allocator<fuzzer::SizedFile> >&) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x384e39)
    #7 0x372ebe in fuzzer::FuzzerDriver(int*, char***, int (*)(unsigned char const*, unsigned long)) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x372ebe)
    #8 0x39c952 in main (/home/doom/stqam/fb/build7/src/doom_fuzz+0x39c952)
    #9 0x7fcbd75abbf6 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21bf6)

Direct leak of 51 byte(s) in 1 object(s) allocated from:
    #0 0x4485cd in malloc (/home/doom/stqam/fb/build7/src/doom_fuzz+0x4485cd)
    #1 0x4dca23 in M_StringJoin /home/doom/stqam/fb/build7/../chocolate-doom/src/m_misc.c:575:14
    #2 0x49fc09 in M_LoadDefaults /home/doom/stqam/fb/build7/../chocolate-doom/src/m_config.c:2111:15
    #3 0x477f07 in LLVMFuzzerTestOneInput /home/doom/stqam/fb/build7/../src/fuzz_target.c:167:3
    #4 0x382a71 in fuzzer::Fuzzer::ExecuteCallback(unsigned char const*, unsigned long) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x382a71)
    #5 0x3821b5 in fuzzer::Fuzzer::RunOne(unsigned char const*, unsigned long, bool, fuzzer::InputInfo*, bool*) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x3821b5)
    #6 0x384457 in fuzzer::Fuzzer::MutateAndTestOne() (/home/doom/stqam/fb/build7/src/doom_fuzz+0x384457)
    #7 0x385155 in fuzzer::Fuzzer::Loop(std::__Fuzzer::vector<fuzzer::SizedFile, fuzzer::fuzzer_allocator<fuzzer::SizedFile> >&) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x385155)
    #8 0x372ebe in fuzzer::FuzzerDriver(int*, char***, int (*)(unsigned char const*, unsigned long)) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x372ebe)
    #9 0x39c952 in main (/home/doom/stqam/fb/build7/src/doom_fuzz+0x39c952)
    #10 0x7fcbd75abbf6 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21bf6)

Direct leak of 51 byte(s) in 1 object(s) allocated from:
    #0 0x4485cd in malloc (/home/doom/stqam/fb/build7/src/doom_fuzz+0x4485cd)
    #1 0x4dca23 in M_StringJoin /home/doom/stqam/fb/build7/../chocolate-doom/src/m_misc.c:575:14
    #2 0x49fc09 in M_LoadDefaults /home/doom/stqam/fb/build7/../chocolate-doom/src/m_config.c:2111:15
    #3 0x477f07 in LLVMFuzzerTestOneInput /home/doom/stqam/fb/build7/../src/fuzz_target.c:167:3
    #4 0x382a71 in fuzzer::Fuzzer::ExecuteCallback(unsigned char const*, unsigned long) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x382a71)
    #5 0x3821b5 in fuzzer::Fuzzer::RunOne(unsigned char const*, unsigned long, bool, fuzzer::InputInfo*, bool*) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x3821b5)
    #6 0x384991 in fuzzer::Fuzzer::ReadAndExecuteSeedCorpora(std::__Fuzzer::vector<fuzzer::SizedFile, fuzzer::fuzzer_allocator<fuzzer::SizedFile> >&) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x384991)
    #7 0x384e39 in fuzzer::Fuzzer::Loop(std::__Fuzzer::vector<fuzzer::SizedFile, fuzzer::fuzzer_allocator<fuzzer::SizedFile> >&) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x384e39)
    #8 0x372ebe in fuzzer::FuzzerDriver(int*, char***, int (*)(unsigned char const*, unsigned long)) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x372ebe)
    #9 0x39c952 in main (/home/doom/stqam/fb/build7/src/doom_fuzz+0x39c952)
    #10 0x7fcbd75abbf6 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21bf6)

Direct leak of 50 byte(s) in 1 object(s) allocated from:
    #0 0x434974 in strdup (/home/doom/stqam/fb/build7/src/doom_fuzz+0x434974)
    #1 0x4db830 in M_StringDuplicate /home/doom/stqam/fb/build7/../chocolate-doom/src/m_misc.c:423:14
    #2 0x4db830 in M_FileCaseExists /home/doom/stqam/fb/build7/../chocolate-doom/src/m_misc.c:93:16
    #3 0x4788d8 in D_FindWADByName /home/doom/stqam/fb/build7/../chocolate-doom/src/d_iwad.c:794:13
    #4 0x47904b in D_FindIWAD /home/doom/stqam/fb/build7/../chocolate-doom/src/d_iwad.c:888:18
    #5 0x477f22 in LLVMFuzzerTestOneInput /home/doom/stqam/fb/build7/../src/fuzz_target.c:173:14
    #6 0x382a71 in fuzzer::Fuzzer::ExecuteCallback(unsigned char const*, unsigned long) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x382a71)
    #7 0x3847aa in fuzzer::Fuzzer::ReadAndExecuteSeedCorpora(std::__Fuzzer::vector<fuzzer::SizedFile, fuzzer::fuzzer_allocator<fuzzer::SizedFile> >&) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x3847aa)
    #8 0x384e39 in fuzzer::Fuzzer::Loop(std::__Fuzzer::vector<fuzzer::SizedFile, fuzzer::fuzzer_allocator<fuzzer::SizedFile> >&) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x384e39)
    #9 0x372ebe in fuzzer::FuzzerDriver(int*, char***, int (*)(unsigned char const*, unsigned long)) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x372ebe)
    #10 0x39c952 in main (/home/doom/stqam/fb/build7/src/doom_fuzz+0x39c952)
    #11 0x7fcbd75abbf6 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21bf6)

Direct leak of 50 byte(s) in 1 object(s) allocated from:
    #0 0x434974 in strdup (/home/doom/stqam/fb/build7/src/doom_fuzz+0x434974)
    #1 0x4db830 in M_StringDuplicate /home/doom/stqam/fb/build7/../chocolate-doom/src/m_misc.c:423:14
    #2 0x4db830 in M_FileCaseExists /home/doom/stqam/fb/build7/../chocolate-doom/src/m_misc.c:93:16
    #3 0x4788d8 in D_FindWADByName /home/doom/stqam/fb/build7/../chocolate-doom/src/d_iwad.c:794:13
    #4 0x47904b in D_FindIWAD /home/doom/stqam/fb/build7/../chocolate-doom/src/d_iwad.c:888:18
    #5 0x477f22 in LLVMFuzzerTestOneInput /home/doom/stqam/fb/build7/../src/fuzz_target.c:173:14
    #6 0x382a71 in fuzzer::Fuzzer::ExecuteCallback(unsigned char const*, unsigned long) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x382a71)
    #7 0x3821b5 in fuzzer::Fuzzer::RunOne(unsigned char const*, unsigned long, bool, fuzzer::InputInfo*, bool*) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x3821b5)
    #8 0x384457 in fuzzer::Fuzzer::MutateAndTestOne() (/home/doom/stqam/fb/build7/src/doom_fuzz+0x384457)
    #9 0x385155 in fuzzer::Fuzzer::Loop(std::__Fuzzer::vector<fuzzer::SizedFile, fuzzer::fuzzer_allocator<fuzzer::SizedFile> >&) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x385155)
    #10 0x372ebe in fuzzer::FuzzerDriver(int*, char***, int (*)(unsigned char const*, unsigned long)) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x372ebe)
    #11 0x39c952 in main (/home/doom/stqam/fb/build7/src/doom_fuzz+0x39c952)
    #12 0x7fcbd75abbf6 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21bf6)

Direct leak of 50 byte(s) in 1 object(s) allocated from:
    #0 0x434974 in strdup (/home/doom/stqam/fb/build7/src/doom_fuzz+0x434974)
    #1 0x4db830 in M_StringDuplicate /home/doom/stqam/fb/build7/../chocolate-doom/src/m_misc.c:423:14
    #2 0x4db830 in M_FileCaseExists /home/doom/stqam/fb/build7/../chocolate-doom/src/m_misc.c:93:16
    #3 0x4788d8 in D_FindWADByName /home/doom/stqam/fb/build7/../chocolate-doom/src/d_iwad.c:794:13
    #4 0x47904b in D_FindIWAD /home/doom/stqam/fb/build7/../chocolate-doom/src/d_iwad.c:888:18
    #5 0x477f22 in LLVMFuzzerTestOneInput /home/doom/stqam/fb/build7/../src/fuzz_target.c:173:14
    #6 0x382a71 in fuzzer::Fuzzer::ExecuteCallback(unsigned char const*, unsigned long) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x382a71)
    #7 0x3821b5 in fuzzer::Fuzzer::RunOne(unsigned char const*, unsigned long, bool, fuzzer::InputInfo*, bool*) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x3821b5)
    #8 0x384991 in fuzzer::Fuzzer::ReadAndExecuteSeedCorpora(std::__Fuzzer::vector<fuzzer::SizedFile, fuzzer::fuzzer_allocator<fuzzer::SizedFile> >&) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x384991)
    #9 0x384e39 in fuzzer::Fuzzer::Loop(std::__Fuzzer::vector<fuzzer::SizedFile, fuzzer::fuzzer_allocator<fuzzer::SizedFile> >&) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x384e39)
    #10 0x372ebe in fuzzer::FuzzerDriver(int*, char***, int (*)(unsigned char const*, unsigned long)) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x372ebe)
    #11 0x39c952 in main (/home/doom/stqam/fb/build7/src/doom_fuzz+0x39c952)
    #12 0x7fcbd75abbf6 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21bf6)

Direct leak of 40 byte(s) in 1 object(s) allocated from:
    #0 0x434974 in strdup (/home/doom/stqam/fb/build7/src/doom_fuzz+0x434974)
    #1 0x4dc160 in M_StringDuplicate /home/doom/stqam/fb/build7/../chocolate-doom/src/m_misc.c:423:14
    #2 0x4a1fc8 in GetDefaultConfigDir /home/doom/stqam/fb/build7/../chocolate-doom/src/m_config.c:2289:16
    #3 0x4a1fc8 in M_SetConfigDir /home/doom/stqam/fb/build7/../chocolate-doom/src/m_config.c:2314:21
    #4 0x477ed1 in LLVMFuzzerTestOneInput /home/doom/stqam/fb/build7/../src/fuzz_target.c:157:3
    #5 0x382a71 in fuzzer::Fuzzer::ExecuteCallback(unsigned char const*, unsigned long) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x382a71)
    #6 0x3821b5 in fuzzer::Fuzzer::RunOne(unsigned char const*, unsigned long, bool, fuzzer::InputInfo*, bool*) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x3821b5)
    #7 0x384457 in fuzzer::Fuzzer::MutateAndTestOne() (/home/doom/stqam/fb/build7/src/doom_fuzz+0x384457)
    #8 0x385155 in fuzzer::Fuzzer::Loop(std::__Fuzzer::vector<fuzzer::SizedFile, fuzzer::fuzzer_allocator<fuzzer::SizedFile> >&) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x385155)
    #9 0x372ebe in fuzzer::FuzzerDriver(int*, char***, int (*)(unsigned char const*, unsigned long)) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x372ebe)
    #10 0x39c952 in main (/home/doom/stqam/fb/build7/src/doom_fuzz+0x39c952)
    #11 0x7fcbd75abbf6 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21bf6)

Direct leak of 40 byte(s) in 1 object(s) allocated from:
    #0 0x434974 in strdup (/home/doom/stqam/fb/build7/src/doom_fuzz+0x434974)
    #1 0x4dc160 in M_StringDuplicate /home/doom/stqam/fb/build7/../chocolate-doom/src/m_misc.c:423:14
    #2 0x4a1fc8 in GetDefaultConfigDir /home/doom/stqam/fb/build7/../chocolate-doom/src/m_config.c:2289:16
    #3 0x4a1fc8 in M_SetConfigDir /home/doom/stqam/fb/build7/../chocolate-doom/src/m_config.c:2314:21
    #4 0x477ed1 in LLVMFuzzerTestOneInput /home/doom/stqam/fb/build7/../src/fuzz_target.c:157:3
    #5 0x382a71 in fuzzer::Fuzzer::ExecuteCallback(unsigned char const*, unsigned long) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x382a71)
    #6 0x3821b5 in fuzzer::Fuzzer::RunOne(unsigned char const*, unsigned long, bool, fuzzer::InputInfo*, bool*) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x3821b5)
    #7 0x384991 in fuzzer::Fuzzer::ReadAndExecuteSeedCorpora(std::__Fuzzer::vector<fuzzer::SizedFile, fuzzer::fuzzer_allocator<fuzzer::SizedFile> >&) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x384991)
    #8 0x384e39 in fuzzer::Fuzzer::Loop(std::__Fuzzer::vector<fuzzer::SizedFile, fuzzer::fuzzer_allocator<fuzzer::SizedFile> >&) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x384e39)
    #9 0x372ebe in fuzzer::FuzzerDriver(int*, char***, int (*)(unsigned char const*, unsigned long)) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x372ebe)
    #10 0x39c952 in main (/home/doom/stqam/fb/build7/src/doom_fuzz+0x39c952)
    #11 0x7fcbd75abbf6 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21bf6)

Direct leak of 40 byte(s) in 1 object(s) allocated from:
    #0 0x434974 in strdup (/home/doom/stqam/fb/build7/src/doom_fuzz+0x434974)
    #1 0x4dc160 in M_StringDuplicate /home/doom/stqam/fb/build7/../chocolate-doom/src/m_misc.c:423:14
    #2 0x4a1fc8 in GetDefaultConfigDir /home/doom/stqam/fb/build7/../chocolate-doom/src/m_config.c:2289:16
    #3 0x4a1fc8 in M_SetConfigDir /home/doom/stqam/fb/build7/../chocolate-doom/src/m_config.c:2314:21
    #4 0x477ed1 in LLVMFuzzerTestOneInput /home/doom/stqam/fb/build7/../src/fuzz_target.c:157:3
    #5 0x382a71 in fuzzer::Fuzzer::ExecuteCallback(unsigned char const*, unsigned long) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x382a71)
    #6 0x3847aa in fuzzer::Fuzzer::ReadAndExecuteSeedCorpora(std::__Fuzzer::vector<fuzzer::SizedFile, fuzzer::fuzzer_allocator<fuzzer::SizedFile> >&) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x3847aa)
    #7 0x384e39 in fuzzer::Fuzzer::Loop(std::__Fuzzer::vector<fuzzer::SizedFile, fuzzer::fuzzer_allocator<fuzzer::SizedFile> >&) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x384e39)
    #8 0x372ebe in fuzzer::FuzzerDriver(int*, char***, int (*)(unsigned char const*, unsigned long)) (/home/doom/stqam/fb/build7/src/doom_fuzz+0x372ebe)
    #9 0x39c952 in main (/home/doom/stqam/fb/build7/src/doom_fuzz+0x39c952)
    #10 0x7fcbd75abbf6 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21bf6)

SUMMARY: AddressSanitizer: 1629 byte(s) leaked in 102 allocation(s).
INFO: to ignore leaks on libFuzzer side use -detect_leaks=0.

They are the bugs I found, but I haven't tried them on chocolate-doom
## Did you manage to compile the game and play it on your local machine (Not inside Docker)?
I did try to compile the game, and I found it was really confused. I honestly don't know what I should do.
