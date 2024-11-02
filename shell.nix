{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs;  [
    xclip
    python3Packages.requests
    python3
  ];

  shellHook = ''
    export IDK_GROQ_API_KEY="KEY"
  '';
}
