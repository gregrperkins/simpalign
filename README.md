# Simpalign

#### for SublimeText2

If you're a visual person who's heard of `⌘ d`,
maybe, when you want to align,
you end up selecting a bunch of things,
then, realizing the world's broken, give up and leave it alone.
Now you too can align.

Select all the `// ==>`'s in the following code:

```javascript
[
'end', // ==> 'mocha.end'
'fail', // ==> 'mocha.fail'
'hook end', // ==> 'mocha.hook_end'
'hook', // ==> 'mocha.hook'
'pass', // ==> 'mocha.pass'
'pending', // ==> 'mocha.pending'
'start', // ==> 'mocha.start'
'suite end', // ==> 'mocha.suite_end'
'suite', // ==> 'mocha.suite'
'test end', // ==> 'mocha.test_end'
'test', // ==> 'mocha.test'
].forEach(function (type) {
```

Hit `⌘ ⌥ l`.

```javascript
[
'end',       // ==> 'mocha.end'
'fail',      // ==> 'mocha.fail'
'hook end',  // ==> 'mocha.hook_end'
'hook',      // ==> 'mocha.hook'
'pass',      // ==> 'mocha.pass'
'pending',   // ==> 'mocha.pending'
'start',     // ==> 'mocha.start'
'suite end', // ==> 'mocha.suite_end'
'suite',     // ==> 'mocha.suite'
'test end',  // ==> 'mocha.test_end'
'test',      // ==> 'mocha.test'
].forEach(function (type) {
```

### Installation

Paste at a shell:

```shell
(cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/ && [ -d Simpalign ] || git clone git@github.com:gregrperkins/simpalign.git )
```

### References

If you like to get fancy, you're probably looking for:
* [https://github.com/khiltd/Abacus](https://github.com/khiltd/Abacus)
* [https://github.com/wbond/sublime_alignment](https://github.com/wbond/sublime_alignment)
* [https://github.com/jlong64/sublime_valign](https://github.com/jlong64/sublime_valign)
* [https://github.com/randy3k/AlignTab](https://github.com/randy3k/AlignTab)
* [https://github.com/SublimeText/ElasticTabstops](https://github.com/SublimeText/ElasticTabstops)
* [https://github.com/NicholasBuse/sublime_CodeAlignment](https://github.com/NicholasBuse/sublime_CodeAlignment)

Props to khiltd and wbond for their work, as it enabled this plugin.
