# Using Puppet, install flask from pip3.
package { 'python-pip3':
    ensure  => 'installed',
}

exec { 'install_flask':
    command => '/usr/bin/pip3 install flask==2.1.0',
    path    => '/usr/local/bin:/usr/bin',
    require => Package['python3-pip'],
}
