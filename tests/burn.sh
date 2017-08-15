#! /bin/sh
cms robot probe >> inventory.txt
tail inventory.txt
cms robot flash erase
cms robot flash python
cms robot credentials put
cms robot put tests/boot.py boot.py

