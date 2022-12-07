puts STDIN.gets.strip.chars.each_cons(14).find_index{ _1.uniq.size == 14 } + 14
