{ pkgs ? import <nixpkgs> {} }:

pkgs.python3Packages.buildPythonPackage rec {
  pname = "idk";
  version = "0.0.1";

  src = ./.; 

  dependencies = [ pkgs.python3Packages.requests ];

  installPhase = ''
    mkdir -p $out/bin
    cp idk.py $out/bin/idk
    substituteInPlace $out/bin/idk --replace-fail "/usr/bin/env python" "${pkgs.python3}/bin/python3"
    substituteInPlace $out/bin/idk --replace-warn "xclip" "${pkgs.xclip}/bin/xclip"
    chmod +x $out/bin/idk
  '';

  meta = with pkgs.lib; {
    description = "CLI tool to fetch Linux commands based on user queries, using Groq API.";
    license = licenses.mit;
    platforms = platforms.linux;
  };
}
