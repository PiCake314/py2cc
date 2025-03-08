#include <print>
#include <string>
#include <vector>
#include <ranges>

using namespace std::literals;

auto greet(const auto& name) {
	std::println("{} {}", "Hello,"s, name);
}

int main()
{
	greet("Ali"s);
}


