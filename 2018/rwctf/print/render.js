const {Router} = require('express')
const {matchesUA} = require('browserslist-useragent')
const router = Router()
const axios = require('axios')
const md = require('../../plugins/md_srv')
// RCE & SSRF

router.post('/render', function (req, res, next) {
  let ret = {}
  ret.ssr = !matchesUA(req.body.ua, {
    browsers: ["last 1 version", "> 1%", "IE 10"],
    _allowHigherVersions: true
  });
  if (ret.ssr) {
    axios(req.body.url).then(r => {
          ret.mdbody = md.render(r.data)
          ret.mdbody = 'axios'
      res.json(ret)
    })
  }
  else {
    ret.mdbody = md.render('# 请稍候…')
    res.json(ret)
  }
});