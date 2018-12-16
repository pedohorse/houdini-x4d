WIP!!
Nothing here is final, everything is a subject to change, so plz have patience till release

## Instructions
Two options:
* just copy otls to your `/home/username/houdiniXX.Y/otls` folder and you are good to go
* to be able to autoupdate: 
  1. find a perfect spot for it, like `/home/username/houdini-tools`, open terminal and `cd` into that dir
  2. type `git clone https://github.com/pedohorse/houdini-x4d.git`, a houdini-x4d dir will be created - `cd` there
  3. type `git checkout dev`
  4. redact your `houdini.env` file located in `/home/username/houdiniXX.Y/` to have a line like: `HOUDINI_PATH=/home/username/houdini-tools;$HOUDINI_PATH;&` (remember to use `;` on windows and `:` on linux/mac, though houdini seem to forgive that mistake if made) (and additional & in the end is not needed if it is already present in `$HOUDINI_PATH` set previously in `houdini.env`)
  * So now any time you want to update to the latest dev branch from github, you just open a terminal, cd to `/home/username/houdini-tools`, type `git fetch && git pull` and that's it !
