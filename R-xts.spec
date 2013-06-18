%global packname  xts
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.9.3
Release:          2
Summary:          eXtensible Time Series
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/xts_0.9-3.tar.gz
Requires:         R-zoo 
Requires:         R-timeSeries R-timeDate R-tseries R-its R-chron R-fts R-tis 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-zoo
BuildRequires:    R-timeSeries R-timeDate R-tseries R-its R-chron R-fts R-tis 

%description
Provide for uniform handling of R's different time-based data classes by
extending zoo, maximizing native format information preservation and
allowing for user level customization and extension, while simplifying
cross-class interoperability.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/api_example
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/unitTests
