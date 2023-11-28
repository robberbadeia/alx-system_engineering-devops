#!/usr/bin/env ruby
#Find the regular expression that will match the above cases

puts ARGV[0].scan(/hbn | hbt{1,}n/).join