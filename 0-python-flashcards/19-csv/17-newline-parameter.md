# Newline Parameter

**Q:** Why use newline='' when opening CSV files?

**A:** Lets the csv module handle line endings correctly (prevents issues with quoted fields containing newlines)
