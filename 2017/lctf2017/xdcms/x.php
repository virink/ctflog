<?php

if(isset($_GET['t'])){
    srand(strftime($_GET['t']));
}
    
    $admin = "xdsec"."###".str_shuffle('you_are_the_member_of_xdsec_here_is_your_flag');
    $code = "xdsec###";
    // $rs = preg_match('/^(xdsec)((?:###|\w)+)$/i', $code, $matches);
    print_r($admin);
    // print_r("xdsec###_ryshum_idurr_xfr_a_gsem__eheeeeto_aeflooycb_");
    // print_r(time());
    // print_r($matches);
    // print_r($matches[0]);
    // print_r($matches[0]===$admin);
    // print_r(count($matches)===3);
    print_r(getrandmax());
