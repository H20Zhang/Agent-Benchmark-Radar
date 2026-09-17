from copy import deepcopy
from pathlib import Path
import sys
import unittest
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from validate_reading import validate_record_time_contract

class SourcePrecisionContractTest(unittest.TestCase):
    def record(self):
        return dict(id='day-source', released='2026-06-03', first_public_at='2026-06-03',
            published_at='2026-06-03', published_at_precision='day',
            first_seen_at='2026-09-17T14:00:00Z', radar_published_at='2026-09-17T15:00:00Z',
            time_provenance='native_v2', map_delta='early_signal',
            release_date_evidence={'first_public_at':{'precision':'day', 'source':'https://example.org/official', 'status':'checked'}})
    def test_explicit_verified_day_retains_source_precision(self):
        self.assertEqual([],validate_record_time_contract(self.record()))
    def test_explicit_verified_month_retains_source_precision(self):
        r=self.record(); r.update(released='2026-06',first_public_at='2026-06',published_at='2026-06',published_at_precision='month')
        r['release_date_evidence']['first_public_at']['precision']='month'
        self.assertEqual([],validate_record_time_contract(r))
    def test_untagged_native_date_still_requires_strict_utc(self):
        r=self.record(); del r['published_at_precision']
        self.assertTrue(validate_record_time_contract(r))
    def test_invalid_calendar_date_is_rejected(self):
        r=self.record(); r.update(released='2026-02-30',first_public_at='2026-02-30',published_at='2026-02-30')
        self.assertTrue(validate_record_time_contract(r))
    def test_future_interval_is_rejected(self):
        r=self.record(); r.update(released='2027-06-03',first_public_at='2027-06-03',published_at='2027-06-03')
        self.assertTrue(validate_record_time_contract(r))
    def test_discovery_and_acceptance_still_require_strict_utc(self):
        for field in ('first_seen_at','radar_published_at'):
            r=self.record(); r[field]='2026-09-17'
            self.assertTrue(validate_record_time_contract(r))
    def test_precision_requires_matching_verified_date_evidence(self):
        for field,value in [('precision','month'),('status','unverified'),('source','')]:
            r=self.record(); r['release_date_evidence']['first_public_at'][field]=value
            self.assertTrue(validate_record_time_contract(r))
        r=self.record(); r['first_public_at']='2026-06-04'
        self.assertTrue(validate_record_time_contract(r))
    def test_precision_alone_triggers_complete_bundle(self):
        self.assertTrue(validate_record_time_contract({'id':'partial','published_at_precision':'day'}))
    def test_legacy_record_cannot_use_native_precision_extension(self):
        r=self.record(); r.update(time_provenance='legacy_unknown',first_seen_at=None,radar_published_at=None)
        self.assertTrue(validate_record_time_contract(r))
    def test_precision_cannot_disguise_exact_time_or_unknown_unit(self):
        for value in ('hour','second',None):
            r=self.record(); r['published_at_precision']=value
            self.assertTrue(validate_record_time_contract(r))
        r=self.record(); r['published_at']='2026-06-03T00:00:00Z'
        self.assertTrue(validate_record_time_contract(r))
