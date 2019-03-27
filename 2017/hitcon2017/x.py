if __name__ == '__main__':
    a = "system('ls')"
    for i in a:
        print "#{%s.chr}" % ord(i),

#{115.chr}#{121.chr}#{115.chr}#{116.chr}#{101.chr}#{109.chr}#{40.chr}#{39.chr}#{108.chr}#{115.chr}#{39.chr}#{41.chr}
