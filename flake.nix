{
  description = "For the most part, this ocbciasonally works";

  inputs.nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";

  outputs = { self, nixpkgs }:
    let pkgs = import nixpkgs { system = "x86_64-linux"; };
    in {
      devShells.x86_64-linux = {
        default = pkgs.mkShell rec {
          nativeBuildInputs = with pkgs; [
            python312
            python312Packages.hatchling
            python312Packages.parsy
          ];
          buildInputs = [ pkgs.uv pkgs.ruff pkgs.python312 ];
          LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath buildInputs;
        };
      };
    };
}
