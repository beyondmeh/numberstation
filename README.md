# numberstation

> Decrypt Bitmessage number spam

For those that are unfamiliar with it, [Bitmessage](https://bitmessage.org/wiki/Main_Page) 
is a P2P encrypted messager similar to Tox, TorChat, Ricochet, etc.

One of the annoyances for new users are reoccurring "number spam" messages. 
These scripts can decode and make those messages.


## Usage

```console
$ echo -n "Hello World" | ./encode.py
```

```console
$ echo -n "72208 65379 71355 84563 47101 72803 26503 60309 50914 50146 90778" | ./decode.py
```

## History
Around the beginning of 2016, mysterious number only messages started being 
spammed to various Bitmessage chans. The sender's address was always different, 
making blocking difficult. The subject was typically a MD5 hash with the message 
looking similar to the following:

> 94445 69192 93958 86475 90202 43920 88888 51721 61057 91423 
> 96933 15468 39109 83028 64371 98156 78594 78587 34576 26908 
> 76175 48800 98662 20945 49004 50009 10896 93713 68187 92822 
> 15972 86723 

Several weeks later, a message in broken Russian seemed to hint how to decode 
the messages. I ended up successfully decoding some, but was let down as they 
ended up being a dirty limericks. The result of my efforts are these two python 
scripts that can encode and decode similar messages.


## Changelog

* 2016-11-05: Added shebang so CLI usage is easier
* 2016-07-19: Creaded encoder (gist)
* 2016-07-18: Created decoder (gist)


## Feedback
I haven't used Bitmessage in a while, but you can contact me by [email](mailto:timothykeith@gmail.com).


### PGP Key
For the privacy conscious, feel free to encrypt any messages using my 
[PGP key](http://pgp.mit.edu/pks/lookup?op=vindex&fingerprint=on&search=0xF4F4A135C022EE12):
> 4135 C593 1D89 368E 7F32 C8ED F4F4 A135 C022 EE12

To import it into your keyring:
```console
$  gpg --keyserver pgp.mit.edu --recv-key 4135C5931D89368E7F32C8EDF4F4A135C022EE12
```


## License

Copyright &copy; 2016 Timothy Keith

Licensed under the [MIT license](https://github.com/keithieopia/numberspam/blob/master/LICENSE).

*This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.*
