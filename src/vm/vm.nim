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
]#

# Imports
import std/os
import system/io

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

# Attempt to read the main file
try:
  let f = open("test.txt")
  var buf: array[6, byte]
  f.readBytes(buf, 8)

except CatchableError:
  echo "[VM ERROR]: The main file does not exist, touch the main.chnl file if you are on unix based systems. Thanks bye :]"