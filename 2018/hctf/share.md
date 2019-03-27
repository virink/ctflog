## Share

### URL

http://share.2018.hctf.io

### 描述 

I have built an app sharing platform, welcome to share your favorite apps for everyone

### Hint

hint1:https://paste.ubuntu.com/p/VfJDq7Vtqf/ 
Alpha_test code:https://paste.ubuntu.com/p/qYxWmZRndR/

### Work

Server: Ruby (erb)

### Dir

views
|-- devise
|   |-- confirmations
|   |-- mailer
|   |-- passwords
|   |-- registrations
|   |   |-- new.html.erb
|   |-- sessions
|   |   |-- new.html.erb
|   |-- shared
|   |-- unlocks
|-- file
|-- home
|   |-- Alphatest.erb
|   |-- addtest.erb
|   |-- home.erb
|   |-- index.html.erb
|   |-- publiclist.erb
|   |-- share.erb
|   |-- upload.erb
|-- layouts
|   |-- application.html.erb
|   |-- mailer.html.erb
|   |-- mailer.text.erb
|-- recommend
     |-- show.erb

### Alpha_test code

	# post /file/Alpha_test
	def Alpha_test
	if(params[:fid] != "" && params[:uid] != "" && params[:fid] != nil && params[:uid] != nil)
	  fid = params[:fid].to_i
	  uid = params[:uid].to_i
	  if(fid > 0 && uid > 0)
	    if(Sharelist.find_by(sharefile_id: fid)==nil)
	      if(Sharelist.count("user_id ="+ uid.to_s) <5)
	        share = Sharelist.new
	        share.sharefile_id = fid
	        share.user_id = uid
	        share.save
	      end
	    end
	  end
	end
	redirect_to(root_path)
	end

## URL2FUNC

- http://share.2018.hctf.io/home/Alphatest
	- show file number:2 your uid: 8
- http://share.2018.hctf.io/home/share
	- Share to admin
	- Context
	- url