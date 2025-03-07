#include <print>
#include <string>
#include <vector>
#include <ranges>

using namespace std::literals;


int main() {
	auto x = true;
	if (false) ;	// pass
	if (x) ;	// pass
	else ;	// pass
}


