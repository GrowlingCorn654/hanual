#[
Nim VM, Virtual machine for compiling and interepreting the hanual bytecode. It is speedy as nim is complied to C.
!! DO NOT CHANGE THIS UNLESS YOU KNOW WHAT YOU'RE DOING !!
== CONFIGUARTION FOR THE VM CAN BE FOUND IN vm.conig ==

        # File extension (Not related to chernobal)
        .chnl

        # Docs links & References
        https://nim-lang.org/docs/manual.html#exception-handling
        https://nim-lang.org/docs/manual.html#statements-and-expressions-while-statement
        https://nim-lang.org/docs/os.html
        https://nim-lang.org/docs/tut2.html#exceptions-raise-statement
        https://stackoverflow.com/questions/34427858/reading-bytes-from-many-files-performance
        https://nim-lang.org/docs/io.html
        https://nim-lang.org/docs/streams.html
        https://nim-lang.org/docs/streams.html#readData%2CStream%2Cpointer%2Cint
]#

# Imports
import std/os # "OS" functions
import system/io # System level i/o
import std/streams # File and input streams

# Add in the registers
let A = "" # General purpose value store
let B = "" # General purpose value store
let C = "" # General purpose value store
let D = "" # General purpose value store
let E = "" # General purpose value store
let G = "" # General purpose value store

let F = "" # This register stores integers that will act as flags for the next instruction
let S = "" # This register stores the status of the last instruction
let O = "" # This register stores the origin of the previous instruction to act as a return pointer
let R = "" # This register holds the return value of a called function

# Check if the main file exists
let file = "test.txt"
let error_advice = "\n [VM INFO]: There appears to be an error in executing your program, please check the hanual VM error doumentation for further details -> https://github.com/Goof-Labs/hanual/wiki/Errors-&-Warnings"

try:
  var strm = openFileStream(file)
  let output = strm.readLine()
  echo "[VM Success] Main file exists! Executing..."
  strm.close()

except:
  let digest = getCurrentExceptionMsg()
  echo "[VM ERROR]: The main file does not exist or cannot be read/opended, touch the main.chnl file if you are on unix based system or re-compile/compile your hanual program. Thanks bye :] \n"
  echo "Error Digest: ", digest
  echo error_advice
  quit(2)

# RUN the bytecode
# 20 bytes is header, first 4 is the magic number. Dump/ignore everything else in the header for now.
var strm = openFileStream(file, fmRead)
var line = ""
if not isNil(strm):
  while strm.readLine(line):
    echo line
  strm.close()