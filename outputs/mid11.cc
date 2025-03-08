#include <print>
#include <string>
#include <vector>
#include <ranges>

using namespace std::literals;


int main()
{
	auto x = true;
	if (false) ;	// "pass". Separate line to silence warning.
	if (x) ;	// "pass". Separate line to silence warning.
	else ;	// "pass". Separate line to silence warning.
}


