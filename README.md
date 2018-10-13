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
