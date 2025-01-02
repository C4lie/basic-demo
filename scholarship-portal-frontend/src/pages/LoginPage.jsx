import jwt_decode from 'jwt-decode';

const handleLogin = async (e) => {
  e.preventDefault();
  try {
    const response = await axios.post('http://localhost:8000/api/users/login/', {
      username,
      password,
    });
    const { access } = response.data;

    localStorage.setItem('access_token', access);

    // Decode the JWT to get the role
    const decoded = jwt_decode(access);
    const role = decoded.role;

    if (role === 'student') {
      navigate('/student-dashboard');
    } else if (role === 'donor') {
      navigate('/donor-dashboard');
    } else if (role === 'admin') {
      navigate('/admin-dashboard');
    }
  } catch (error) {
    setError('Invalid credentials');
  }
};
