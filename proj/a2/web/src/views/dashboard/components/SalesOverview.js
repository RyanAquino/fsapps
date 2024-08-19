import React, { useEffect, useState } from 'react';
import { Select, MenuItem } from '@mui/material';
import { useTheme } from '@mui/material/styles';
import DashboardCard from '../../../components/shared/DashboardCard';
import Chart from 'react-apexcharts';
import { dtsTable } from '../../../api/utils';
import { useNavigate } from 'react-router-dom';

const SalesOverview = () => {
  const [tableData, setTableData] = useState([]);
  const navigate = useNavigate();
  const loginRoute = '/auth/login';

  useEffect(() => {
    const token = localStorage.getItem('token');

    if (!token) {
      navigate(loginRoute);
    }

    const fetchTableData = async () =>
      await dtsTable(token, 'operating_cash_balance').catch((err) => {
        console.log(err);
        if (err.response.status === 401) {
          navigate(loginRoute);
        }
      });
    fetchTableData().then((tableData) => {
      let data = [];
      let dates = [];

      for (const item of tableData) {
        if (dates.includes(item['record_date'])) {
          continue;
        }
        dates.push(item['record_date']);
        data.push({
          net_change: item['net_change'],
          date: item['record_date'],
        });
      }
      setTableData(data);
    });
  }, []);

  // select
  const [month, setMonth] = useState('1');

  const handleChange = (event) => {
    setMonth(event.target.value);
  };

  // chart color
  const theme = useTheme();
  const primary = theme.palette.primary.main;
  const secondary = theme.palette.secondary.main;

  // chart
  const optionscolumnchart = {
    chart: {
      height: 350,
      type: 'line',
      dropShadow: {
        enabled: true,
        color: '#000',
        top: 18,
        left: 7,
        blur: 10,
        opacity: 0.2,
      },
      zoom: {
        enabled: false,
      },
      toolbar: {
        show: false,
      },
    },
    colors: [primary, secondary],
    dataLabels: {
      enabled: true,
    },
    stroke: {
      curve: 'smooth',
    },
    title: {
        text: 'Daily net change',
        align: 'left'
    },
    grid: {
      borderColor: '#e7e7e7',
      row: {
        colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
        opacity: 0.5,
      },
    },
    markers: {
      size: 1,
    },
    xaxis: {
      categories: tableData.map((i) => i['date']),
      title: {
        text: 'Day',
      },
    },
    yaxis: {
      title: {
        text: 'Net change',
      },
      min: Math.min(...tableData.map((i) => i['net_change'])),
      max: Math.max(...tableData.map((i) => i['net_change'])),
    },
    legend: {
      position: 'top',
      horizontalAlign: 'right',
      floating: true,
      offsetY: -25,
      offsetX: -5,
    },
  };

  const seriescolumnchart = [
    {
      name: 'Net Change',
      data: tableData.map((i) => i['net_change']),
    },
  ];
  return (
    <DashboardCard
      title="Operating Cash Balance"
    >
      <Chart options={optionscolumnchart} series={seriescolumnchart} type="line" height="270px" />
    </DashboardCard>
  );
};

export default SalesOverview;
