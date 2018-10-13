# Unnecessary Debugging Calls Exterminator, aka `udce`
Meet `udce`, a CLI tool that helps you to find and exterminatate unnecessary debugging calls on your code such as `console.log`, `byebug` and so on.

# Usage
Use it on your terminal:

```sh
$ udce . --language=ruby
Found debugging call on app/mailers/application_mailer.rb:10
    puts "Sending mail to #{params[:to]}"


Found debugging call on app/mailers/application_mailer.rb:34
    puts "Email could not be sent #{e}"
```

# Developing and contributing
To develop and debug `udce`, you'll need Python 3 and PIP.

1) Clone the project
2) Run the following script inside the project root folder: `pip3 install --editable .`
3) You're good to go! Run `udce . --languages=python` to check if everything is fine
