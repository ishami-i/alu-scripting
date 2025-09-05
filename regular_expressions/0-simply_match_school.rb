#!/usr/bin/env ruby
input = ARGV.join(" ")
matches = input.scan(/School/)
puts matches.join
