# unless params[:SECRET].nil?
# if ENV["SECRET"].match("#{params[:SECRET].match(/[0-9a-z]+/)}")
#   puts ENV["FLAG"]
# end
# end
map1 = {
    "do"=>"[\"<%=self%>\", \"1\", \"2\", \"3\", \"4\", \"5\", \"6\"] is working",
    "name"=>["<%=self%>", "1","2","3","4","5","6"]}


puts "map1"
puts map1
puts "\r\n"

puts "map1[\"name\"]"
puts map1["name"]
puts "\r\n"

puts "map1[\"name[0,7]\"]"
puts map1["name"][0,7]
puts "\r\n"

puts "map1[\"do\"]"
puts map1["do"]
puts "\r\n"

puts "map1[\"name[0,7]\"] is working"
puts "#{map1["name"][0,7]} is working"
puts "\r\n"

if map1["do"] == "#{map1["name"][0,7]} is working" then
    puts "<script>alert('#{map1["name"][0,7]} working successfully!')</script>"
end