# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

# print 2 ** 10      # one kilobit, kb
# print 2 ** 10 * 8  # one kilobyte, kB

# print 2 ** 20      # one megabit, Mb
# print 2 ** 20 * 8  # one megabyte, MB

# print 2 ** 30      # one gigabit, Gb
# print 2 ** 30 * 8  # one gigabyte, GB

# print 2 ** 40      # one terabit, Tb
# print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size
# is given in megabytes (MB).


def download_time(file_num, file_unit, bandwidth_num, bandwidth_unit):
    global total_bit_file, total_bit_bandwidth
    tobit = [
        ["kb", 2**10],
        ["kB", 2**10*8],
        ["Mb", 2**20],
        ["MB", 2**20*8],
        ["Gb", 2**30],
        ["GB", 2**30*8],
        ["Tb", 2**40],
        ["TB", 2**40*8]
    ]
    for entry in tobit:
        if entry[0] == file_unit:
            total_bit_file = entry[1] * file_num
        if entry[0] == bandwidth_unit:
            total_bit_bandwidth = entry[1] * bandwidth_num
    dl_seconds = total_bit_file * 1.0 / total_bit_bandwidth
    return convert_seconds(dl_seconds)


def convert_seconds(time):
    hour = int(time // 3600)
    time -= hour * 3600
    minute = int(time // 60)
    time -= minute * 60
    second = time
    result = ""
    if hour == 1:
        result += "1 hour, "
    else:
        result += "%s hours, " % hour
    if minute == 1:
        result += "1 minute, "
    else:
        result += "%s minutes, " % minute
    if second == 1:
        result += "1 second"
    else:
        result += "%s seconds" % second
    return result


print(download_time(1024, 'kB', 1, 'MB'))
# >>> 0 hours, 0 minutes, 1 second

print(download_time(1024, 'kB', 1, 'Mb'))
# >>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print(download_time(13, 'GB', 5.6, 'MB'))
# >>> 0 hours, 39 minutes, 37.1428571429 seconds

print(download_time(13, 'GB', 5.6, 'Mb'))
# >>> 5 hours, 16 minutes, 57.1428571429 seconds

print(download_time(10, 'MB', 2, 'kB'))
# >>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print(download_time(10,'MB', 2, 'kb'))
# >>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable


