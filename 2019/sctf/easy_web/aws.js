const AWS = require("aws-sdk");
const cfg = {
    "Bucket": "static.l0ca1.xyz",
    "host": "static.l0ca1.xyz",
}
const s3Parme = {
    accessKeyId: "ASIA5CRTL2SNIBLFAVHT",
    secretAccessKey: "XxEWYXlnNjVdeesn4mEBiyTXuTUtDW9pQY2aYRFy",
    sessionToken: 'AgoJb3JpZ2luX2VjEH0aDmFwLW5vcnRoZWFzdC0xIkYwRAIgMGsCOi5KSvQRM2sP/SHKAmHiF0qQQImI8xRIYkdwE7ECIDahKwbNkCM7GeyU+GwQftqdHVY4R8DiOrvx+n2JtK9lKokCCLb//////////wEQABoMODk4ODI5NjM2NzYyIgzfFEGdud2jZ17D5fwq3QHoeXy+deg+LFhxa54uTOZlR966/Jk6zuoK85SBa0RG0v8NlBYOYqaT1EBnhvl6sh7GKiyuzBUuHbA64V8T4eeMNt04MG3/YpKaRMJzCxC/RijNPDUjXD0oh/YcM7wDhZbO8pzUzubKHys84H1T6eDbFVstMGtUPeoe4z0xfJN/TTPO8SQ2IJYD2oToJk0rrOnpktWxgTMEJgeYx5kxPaEKxAK0ZOzXHUDwzE56blub9RGI0/LLylYDIXyx5d1AV6ypzeYl0aV+mcL9O9urGp4i/gkevgnadnORguBmpDDa4rboBTq1AWtsIOXozs98y4Yw4v1Et1xea/AA+Ulq/uBFbvOBL3PMzUz/PqgUWiTQBOiRI8gq8yyxfoNLJA8A3ipzT0Wm67XbsKvDNnmfZT5zQOagtPXq3J3yR8+zKbodxwLLxXReItunw8FAaYHk5VbQiTsuXbkqAhtmC+oZi3uiIyLSbK2co/FkGGSWH/JFh7uhAlb+Cl4bfoOdTg9p1HcQEBroZ9dnP7wdgVRFD1vUnJx8yRngghnfiCA='
}
var s3 = new AWS.S3(s3Parme);
data = s3.getObject({
    Bucket: cfg.Bucket,
    Key: `flaaaaaaaaag/flaaaag.txt`,
}).promise().catch(e => {
    console.log(e);
    return;
}).then((e) => {
    console.log(e.Body.toString())
});
// console.log(data)
// // listBuckets
// data = s3.listBuckets({
//     // Bucket: cfg.Bucket,
//     // Key: `flag`,
// }).promise().catch(e => {
//     console.log(e);
//     return;
// }).then((e) => {
//     console.log(e)
// });
// ListObjects
data = s3.listObjectsV2({
    Bucket: cfg.Bucket,
    MaxKeys: 1,
}).promise().catch(e => {
    console.log(e);
    return;
}).then((e) => {
    console.log(e)
});
// ListObjects
// data = s3.listObjectVersions({
//     Bucket: cfg.Bucket,
//     Prefix: "flaaaaaaaaag",
// }).promise().catch(e => {
//     console.log(e);
//     return;
// }).then((e) => {
//     console.log(e)
// });
// console.log(data)