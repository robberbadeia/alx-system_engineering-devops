# increase the requests limit for nginx

exec {'fix_limit':
    # modify the limit
    command => '/bin/sed -i "s/15/4094/" /etc/default/nginx',
    # path of sed command
    path    => '/usr/local/bin/:/bin/',
}

exec {'nginx_restart':
    # nginx restart
    command => '/etc/init.d/nginx restart',
    # init.d path
    path    => '/etc/init.d',
}
